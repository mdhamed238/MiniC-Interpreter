from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from Exo_19Lexer import Exo_19Lexer
from Exo_19Parser import Exo_19Parser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = Exo_19Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Exo_19Parser(stream)
    parser.full_expr()  # We want to recognize full_expr in grammar Exo_19
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
