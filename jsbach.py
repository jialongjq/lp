from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from TreeVisitor import TreeVisitor
import sys

input_stream = FileStream(sys.argv[1], encoding='utf-8')
print(input_stream)

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = jsbachParser(token_stream)
tree = parser.root()

print(tree.toStringTree(recog=parser))

visitor = TreeVisitor()
visitor.visit(tree)
