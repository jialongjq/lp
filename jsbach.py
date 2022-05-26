from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from TreeVisitor import TreeVisitor
import sys
import os
import playsound

input_stream = FileStream(sys.argv[1], encoding='utf-8')
inici = 'Main'
if len(sys.argv) > 2:
    inici = sys.argv[2]
print(input_stream)

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = jsbachParser(token_stream)
tree = parser.root()

print(tree.toStringTree(recog=parser))

partitura = []
visitor = TreeVisitor(inici, partitura)
visitor.visit(tree)
notes = ' '.join(partitura)

with open('partitura.lily', 'w', encoding='ascii') as f:
    f.write('\\version "2.22.1"\n'
            '\\score {\n'
            '    \\absolute {\n'
            '        \\tempo 4 = 120\n'
            "        %s\n"
            '   }\n'
            '   \\layout { }\n'
            '   \\midi { }\n'
            '}\n' % notes)
os.system("lilypond partitura.lily")
os.system("timidity -Ow -o partitura.wav partitura.midi")
os.system("ffmpeg -i partitura.wav -codec:a libmp3lame -qscale:a 2 partitura.mp3")
playsound.playsound("partitura.mp3")
