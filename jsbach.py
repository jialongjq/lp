from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from TreeVisitor import TreeVisitor
import sys
import os
import playsound

if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise Exception('Ús: python3 jsbach.py fitxer.jsb [Procediment]')

nomFitxer, extensioFitxer = os.path.splitext(sys.argv[1])
if extensioFitxer != '.jsb':
    raise Exception("L'extensió dels fitxers per programes en JSBach ha de ser .jsb!")

inici = 'Main'
if len(sys.argv) > 2:
    inici = sys.argv[2]

input_stream = FileStream(sys.argv[1], encoding='utf-8')

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

with open('%s.lily' % nomFitxer, 'w') as f:
    f.write('\\version "2.22.1"\n'
            '\\score {\n'
            '    \\absolute {\n'
            '        \\tempo 4 = 120\n'
            "        %s\n"
            '   }\n'
            '   \\layout { }\n'
            '   \\midi { }\n'
            '}\n' % notes)
os.system("lilypond %s.lily" % nomFitxer)
os.system("timidity -Ow -o %s.wav %s.midi" % (nomFitxer, nomFitxer))
os.system("ffmpeg -i %s.wav -codec:a libmp3lame -qscale:a 2 %s.mp3" % (nomFitxer, nomFitxer))
playsound.playsound("%s.mp3" % nomFitxer)
