# Visitor to *interpret* MiniC files
from typing import (
  Dict,
  List)
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.Errors import MiniCRuntimeError, MiniCInternalError, MiniCTypeError, MiniCUnsupportedError

MINIC_VALUE = int | str | bool | float | List['MINIC_VALUE']


class MiniCInterpretVisitor(MiniCVisitor):

    _memory: Dict[str, MINIC_VALUE]

    def __init__(self):
        self._memory = dict()  # store all variable ids and values.
        self.has_main = False

    # visitors for variable declarations

    def visitVarDecl(self, ctx) -> None:
        # Initialise all variables in self._memory
        type_str = ctx.typee().getText()
        var_list = self.visit(ctx.id_l())
        
        for var_name in var_list:
            match type_str:
                case 'int':
                    self._memory[var_name] = 0
                case 'float':
                    self._memory[var_name] = 0.0
                case 'bool':
                    self._memory[var_name] = False
                case 'string':
                    self._memory[var_name] = ""

        
    def visitIdList(self, ctx) -> List[str]:
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t
        

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # visitors for atoms --> value

    def visitParExpr(self, ctx) -> MINIC_VALUE:
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx) -> int:
        return int(ctx.getText())

    def visitFloatAtom(self, ctx) -> float:
        return float(ctx.getText())

    def visitBooleanAtom(self, ctx) -> bool:
        return ctx.getText() == "true"

    def visitIdAtom(self, ctx) -> MINIC_VALUE:
        return self._memory[ctx.getText()]

    def visitStringAtom(self, ctx) -> str:
        return ctx.getText()[1:-1]  # Remove the ""

    # visit expressions

    def visitAtomExpr(self, ctx) -> MINIC_VALUE:
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx) -> bool:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval | rval

    def visitAndExpr(self, ctx) -> bool:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval & rval

    def visitEqualityExpr(self, ctx) -> bool:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # be careful for float equality
        if ctx.myop.type == MiniCParser.EQ:
            return lval == rval
        else:
            return lval != rval

    def visitRelationalExpr(self, ctx) -> bool:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.LT:
            return lval < rval
        elif ctx.myop.type == MiniCParser.LTEQ:
            return lval <= rval
        elif ctx.myop.type == MiniCParser.GT:
            return lval > rval
        elif ctx.myop.type == MiniCParser.GTEQ:
            return lval >= rval
        else:
            raise MiniCInternalError(
                f"Unknown comparison operator '{ctx.myop}'"
            )

    def visitAdditiveExpr(self, ctx) -> MINIC_VALUE:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.PLUS:
            if any(isinstance(x, str) for x in (lval, rval)):
                return '{}{}'.format(lval, rval)
            else:
                return lval + rval
        elif ctx.myop.type == MiniCParser.MINUS:
            return lval - rval
        else:
            raise MiniCInternalError(
                f"Unknown additive operator '{ctx.myop}'")


    def visitMultiplicativeExpr(self, ctx) -> MINIC_VALUE: # type: ignore
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        
        match ctx.myop.type:
            case MiniCParser.MULT:
                return lval * rval
            case MiniCParser.DIV:
                if rval == 0:
                    raise MiniCRuntimeError("Division by 0")
                return lval / rval;
            case MiniCParser.MOD:
                if rval == 0:
                    raise MiniCRuntimeError("Division by 0")
                q = int(lval / rval)
                return lval - q * rval

    def visitNotExpr(self, ctx) -> bool:
        return not self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx) -> MINIC_VALUE:
        return -self.visit(ctx.expr())

    # visit statements

    def visitPrintlnintStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        assert isinstance(val, int)
        print(val)

    def visitPrintlnfloatStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        assert isinstance(val, float)
        print(f"{val:.2f}")

    def visitPrintlnboolStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        assert isinstance(val, bool)
        print('1' if val else '0')

    def visitPrintlnstringStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        assert isinstance(val, str)
        print(val)

    def visitAssignStat(self, ctx) -> None:
        # Initialise all variables in self._memory
        name = ctx.ID().getText()
        new_value = self.visit(ctx.expr())
        old_value = self._memory[name]
        
        if isinstance(old_value, bool):
            self._memory[name] = bool(new_value)
        elif isinstance(old_value, float):
            self._memory[name] = float(new_value)
        elif isinstance(old_value, int):
            self._memory[name] = int(new_value)
        else: 
            self._memory[name] = new_value
        # print(f"{name} <-- {self._memory[name]} was {old_value}")


    def visitIfStat(self, ctx) -> None:
        if self.visit(ctx.expr()):
            self.visit(ctx.then_block)
        else:
            if ctx.else_block:
                self.visit(ctx.else_block)

    def visitWhileStat(self, ctx) -> None:
        while(self.visit(ctx.expr())):
            self.visit(ctx.body)

    # TOPLEVEL
    def visitProgRule(self, ctx) -> None:
        self.visitChildren(ctx)
        if not self.has_main:
            # A program without a main function is compilable (hence
            # it's not a typing error per se), but not executable,
            # hence we consider it a runtime error.
            raise MiniCRuntimeError("No main function in file")

    # Visit a function: ignore if non main!
    def visitFuncDef(self, ctx) -> None:
        funname = ctx.ID().getText()
        if funname == "main":
            self.has_main = True
            self.visit(ctx.vardecl_l())
            self.visit(ctx.block())
        else:
            raise MiniCUnsupportedError("Functions are not supported in evaluation mode")
