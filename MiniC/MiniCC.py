#! /usr/bin/python3
"""
Evaluation and code generation labs, main file.
Usage:
    python3 MiniCC.py --mode <mode> <filename>
    python3 MiniCC.py --help
"""

from __future__ import annotations

from typing import cast
from enum import Enum

from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from TypingAndInterpret.MiniCTypingVisitor import MiniCTypingVisitor, MiniCTypeError
from TypingAndInterpret.MiniCInterpretVisitor import MiniCInterpretVisitor
from Lib.Errors import (MiniCUnsupportedError, MiniCInternalError,
                        MiniCRuntimeError, AllocationError)

import antlr4
from antlr4.error.ErrorListener import ErrorListener

from argparse import ArgumentParser
from traceback import print_exc
import os
import sys


class Mode(Enum):
    PARSE = 0
    EVAL = 1
    LINEAR = 2
    CFG = 3
    SSA = 4
    OPTIM = 5

    def is_codegen(self) -> bool:
        return self.value >= Mode.LINEAR.value

    def is_ssa(self) -> bool:
        return self.value >= Mode.SSA.value


def valid_modes():
    modes = ['parse', 'typecheck', 'eval']

    try:
        import CodeGen.MiniCCodeGen3AVisitor  # pyright: ignore # noqa: F401, type: ignore
        modes.append('codegen-linear')
    except ModuleNotFoundError:
        return modes

    try:
        import Lib.CFG  # pyright: ignore # noqa: F401, type: ignore
        modes.append('codegen-cfg')
    except ModuleNotFoundError:
        return modes

    try:
        import RegAlloc.EnterSSA  # pyright: ignore # noqa: F401, type: ignore
        modes.append('codegen-ssa')
    except ModuleNotFoundError:
        return modes

    try:
        import TPoptim.OptimSSA  # pyright: ignore # noqa: F401, type: ignore
        modes.append('codegen-optim')
    except ModuleNotFoundError:
        pass

    return modes


class CountErrorListener(ErrorListener):
    """Count number of errors.

    Parser provides getNumberOfSyntaxErrors(), but the Lexer
    apparently doesn't provide an easy way to know if an error occurred
    after the fact. Do the counting ourserves with a listener.
    """

    def __init__(self):
        super(CountErrorListener, self).__init__()
        self.count = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.count += 1


def main(inputname, reg_alloc, mode,
         typecheck=True, stdout=False, output_name=None, debug=False,
         debug_graphs=False, ssa_graphs=False, dom_graphs=False):
    (basename, rest) = os.path.splitext(inputname)
    if mode.is_codegen():
        if stdout:
            output_name = None
            print("Code will be generated on standard output")
        elif output_name is None:
            output_name = basename + ".s"
            print("Code will be generated in file " + output_name)

    input_s = antlr4.FileStream(inputname, encoding='utf-8')
    lexer = MiniCLexer(input_s)
    counter = CountErrorListener()
    lexer._listeners.append(counter)
    stream = antlr4.CommonTokenStream(lexer)
    parser = MiniCParser(stream)
    parser._listeners.append(counter)
    tree = parser.prog()
    if counter.count > 0:
        exit(3)  # Syntax or lexicography errors occurred, don't try to go further.
    if typecheck:
        typing_visitor = MiniCTypingVisitor()
        try:
            typing_visitor.visit(tree)
        except MiniCTypeError as e:
            print(e.args[0])
            exit(2)

    if mode == Mode.EVAL:
        # interpret Visitor
        interpreter_visitor = MiniCInterpretVisitor()
        try:
            interpreter_visitor.visit(tree)
        except MiniCRuntimeError as e:
            print(e.args[0])
            exit(1)
        except MiniCInternalError as e:
            print(e.args[0], file=sys.stderr)
            exit(4)
        return

    if not mode.is_codegen():
        if debug:
            print("Not running code generation because of --typecheck-only.")
        return

    # Codegen 3@ CFG Visitor, first argument is debug mode
    from CodeGen.MiniCCodeGen3AVisitor import MiniCCodeGen3AVisitor  # type: ignore[import]
    visitor3 = MiniCCodeGen3AVisitor(debug, parser)

    # dump generated code on stdout or file.
    with open(output_name, 'w') if output_name else sys.stdout as output:
        visitor3.visit(tree)
        for function in visitor3.get_functions():
            fdata = function.fdata
            # Allocation part
            if mode == Mode.LINEAR:
                code = function
            else:
                from CodeGen.BuildCFG import build_cfg  # type: ignore[import]
                code = build_cfg(function)
            if debug_graphs:
                s = "{}.{}.dot".format(basename, code.fdata.get_name())
                print("CFG:", s)
                code.print_dot(s, view=True)
            if mode.is_ssa():
                from RegAlloc.EnterSSA import enter_ssa  # type: ignore[import]
                from Lib.CFG import CFG  # type: ignore[import]
                enter_ssa(cast(CFG, code), dom_graphs, basename)
                if ssa_graphs:
                    s = "{}.{}.enterssa.dot".format(basename, code.fdata.get_name())
                    print("SSA:", s)
                    code.print_dot(s, view=True)
                if mode == Mode.OPTIM:
                    from TPoptim.OptimSSA import OptimSSA  # type: ignore[import]
                    OptimSSA(cast(CFG, code), debug=debug)
                    if ssa_graphs:
                        s = "{}.{}.optimssa.dot".format(basename, code.fdata.get_name())
                        print("SSA after optim:", s)
                        code.print_dot(s, view=True)
            allocator = None
            if reg_alloc == "naive":
                from Lib.Allocator import NaiveAllocator  # type: ignore[import]
                allocator = NaiveAllocator(fdata)
                comment = "naive allocation"
            elif reg_alloc == "all-in-mem":
                from CodeGen.AllInMemAllocator import AllInMemAllocator  # type: ignore[import]
                allocator = AllInMemAllocator(fdata)
                comment = "all-in-memory allocation"
            elif reg_alloc == "hybrid":
                from CodeGen.HybridNaiveAllocator import (  # type: ignore[import]
                        HybridNaiveAllocator
                )
                allocator = HybridNaiveAllocator(fdata)
                comment = "hybrid, naive allocation"
            elif reg_alloc == "smart":
                liveness = None
                if mode.is_ssa():
                    from RegAlloc.LivenessSSA import LivenessSSA  # type: ignore[import]
                    try:
                        from Lib.CFG import CFG  # type: ignore[import]
                        liveness = LivenessSSA(cast(CFG, code), debug=debug)
                    except NameError:
                        form = "CFG in SSA form"
                        raise ValueError("Invalid dataflow form: \
liveness file not found for {}.".format(form))
                else:
                    try:
                        from RegAlloc.LivenessDataFlow import (  # type: ignore[import]
                                LivenessDataFlow
                        )
                        liveness = LivenessDataFlow(code, debug=debug)
                    except NameError:
                        form = "CFG not in SSA form"
                        raise ValueError("Invalid dataflow form: \
liveness file not found for {}.".format(form))
                from RegAlloc.SmartAllocator import SmartAllocator  # type: ignore[import]
                allocator = SmartAllocator(fdata, basename, liveness,
                                           debug, debug_graphs)
                comment = "smart allocation with graph coloring"
            elif reg_alloc == "none":
                comment = "non executable 3-Address instructions"
            else:
                raise ValueError("Invalid allocation strategy:" + reg_alloc)
            if allocator:
                allocator.prepare()
            if mode.is_ssa():
                from Lib.CFG import CFG  # type: ignore[import]
                from RegAlloc.ExitSSA import exit_ssa  # type: ignore[import]
                exit_ssa(cast(CFG, code), reg_alloc == 'smart')
                comment += " with SSA"
            if allocator:
                allocator.rewriteCode(code)
            if mode.is_ssa() and ssa_graphs:
                s = "{}.{}.exitssa.dot".format(basename, code.fdata.get_name())
                print("CFG after SSA:", s)
                code.print_dot(s, view=True)
            from Lib.LinearCode import LinearCode  # type: ignore[import]
            output.write(f"# Code generated by {os.path.realpath(sys.argv[0])}\n")
            for v in os.environ:
                if v.startswith("REPLACE_"):
                    output.write(f"# {v}={os.environ[v]}\n")
            output.write(f"# Options: {' '.join(sys.argv[1:])}\n")
            if isinstance(code, LinearCode):
                code.print_code(output, comment=comment)
            else:
                from Lib.CFG import CFG  # type: ignore[import]
                from CodeGen.LinearizeCFG import linearize  # type: ignore[import]
                assert (isinstance(code, CFG))
                code.print_code(output, linearize=linearize, comment=comment)
            if debug:
                visitor3.printSymbolTable()


# command line management
if __name__ == '__main__':

    modes = valid_modes()

    parser = ArgumentParser(description='CAP/MIF08 MiniCC compiler')

    parser.add_argument('filename', type=str,
                        help='Source file.')
    parser.add_argument('--mode', type=str,
                        choices=modes,
                        required=True,
                        help='Operation to perform on the input program')
    parser.add_argument('--debug', action='store_true',
                        default=False,
                        help='Emit verbose debug output')
    parser.add_argument('--disable-typecheck', action='store_true',
                        default=False,
                        help="Don't run the typechecker before evaluation or code generation")

    if "codegen-linear" in modes:
        parser.add_argument('--reg-alloc', type=str,
                            choices=['none', 'naive', 'all-in-mem', 'hybrid', 'smart'],
                            help='Register allocation to perform during code generation')
        parser.add_argument('--stdout', action='store_true',
                            help='Generate code to stdout')
        parser.add_argument('--output', type=str,
                            help='Generate code to outfile')

    if "codegen-cfg" in modes:
        parser.add_argument('--graphs', action='store_true',
                            default=False,
                            help='Display graphs (CFG, conflict graph).')

    if "codegen-ssa" in modes:
        parser.add_argument('--ssa-graphs', action='store_true',
                            default=False,
                            help='Display the CFG at SSA entry and exit.')
        parser.add_argument('--dom-graphs', action='store_true',
                            default=False,
                            help='Display dominance-related graphs (DT, DF).')

    args = parser.parse_args()
    reg_alloc = args.reg_alloc if "codegen-linear" in modes else None
    to_stdout = args.stdout if "codegen-linear" in modes else False
    outfile = args.output if "codegen-linear" in modes else None
    graphs = args.graphs if "codegen-cfg" in modes else False
    ssa_graphs = args.ssa_graphs if "codegen-ssa" in modes else False
    dom_graphs = args.dom_graphs if "codegen-ssa" in modes else False

    if reg_alloc is None and "codegen" in args.mode:
        print("error: the following arguments is required: --reg-alloc")
        exit(1)
    elif reg_alloc is not None and "codegen" not in args.mode:
        print("error: register allocation is only available in code generation mode")
        exit(1)

    typecheck = not args.disable_typecheck

    if args.mode == "parse":
        mode = Mode.PARSE
        typecheck = False
    elif args.mode == "typecheck":
        mode = Mode.PARSE
    elif args.mode == "eval":
        mode = Mode.EVAL
    elif args.mode == "codegen-linear":
        mode = Mode.LINEAR
        if reg_alloc == "smart":
            print("error: smart register allocation is not compatible with linear code generation")
            exit(1)
    elif args.mode == "codegen-cfg":
        mode = Mode.CFG
    elif args.mode == "codegen-ssa":
        mode = Mode.SSA
    elif args.mode == "codegen-optim":
        mode = Mode.OPTIM
    else:
        raise ValueError("Invalid mode:" + args.mode)

    try:
        main(args.filename, reg_alloc, mode,
             typecheck,
             to_stdout, outfile, args.debug,
             graphs, ssa_graphs, dom_graphs)
    except MiniCUnsupportedError as e:
        print(e)
        exit(5)
    except (MiniCInternalError, AllocationError):
        print_exc()
        exit(4)
