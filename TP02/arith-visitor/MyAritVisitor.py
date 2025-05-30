from AritVisitor import AritVisitor
from AritParser import AritParser


class UnknownIdentifier(Exception):
    pass


class MyAritVisitor(AritVisitor):
    """Visitor that evaluates an expression. Derives and overrides methods
    from ArithVisitor (generated by ANTLR4)."""
    def __init__(self):
        self._memory = dict()  # store id -> values

    def visitNumberAtom(self, ctx):
        try:
            value = int(ctx.getText())
            return value
        except ValueError:
            return float(ctx.getText())

    def visitIdAtom(self, ctx):
        print('Atom: ', ctx.getText())
        try:
            return self._memory[ctx.getText()]
        except KeyError:
            raise UnknownIdentifier(ctx.getText())

    def visitMultiplicationExpr(self, ctx):
        # Recursive calls to children. The visitor will choose the
        # appropriate method (visitSomething) automatically.
        leftval = self.visit(ctx.expr(0))
        rightval = self.visit(ctx.expr(1))
        print("-MULT- Left eval", leftval)
        print("-MULT- Right eval", rightval)
        # an elegant way to match the token:
        if ctx.multop.type == AritParser.MULT:
            return leftval * rightval
        else:
            return leftval / rightval

    def visitAdditiveExpr(self, ctx):
        leftval = self.visit(ctx.expr(0))
        rightval = self.visit(ctx.expr(1))
        print("-PLUS- Left eval", leftval)
        print("-PLUS- Right eval", rightval)
        if ctx.addop.type == AritParser.PLUS:
            return leftval + rightval
        else:
            return leftval - rightval

    def visitExprInstr(self, ctx):
        val = self.visit(ctx.expr())
        print('The value is ' + str(val))

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitAssignInstr(self, ctx):
        val = self.visit(ctx.expr())
        name = ctx.ID().getText()
        print('now ' + name + ' has value ' + str(val))
        self._memory[name] = val
