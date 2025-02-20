from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from Exo_20Lexer import Exo_20Lexer
from Exo_20Parser import Exo_20Parser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = Exo_20Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Exo_20Parser(stream)
    parser.full_expr()  # We want to recognize full_expr in grammar Exo_20
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
