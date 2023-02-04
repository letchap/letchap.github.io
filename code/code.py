from __future__ import absolute_import
from __future__ import unicode_literals
from . import Extension
from ..preprocessors import Preprocessor
import re
import codecs


# L'expression régulière permettant de trouver le tag dans le texte

CODE_RE = re.compile(r'\{% code ?(?P<src>[^\}]*) \%}')

class CodePreprocessor(Preprocessor):

# Le pré-processor
# Je lis les lignes de mon fichier markdown
# Je les mets une à une dans une liste
# Dès que je trouve une correspondance à mon expression régulière
# J'ouvre le fichier source
# Je le lis ligne à ligne en ajoutant une indentation de 4 espaces pour # le bloc de code markdown
# Je complète ma liste avec ces lignes
# Quand j'ai tout lu, je renvoie la liste pour la suite du traitement
# markdown

    def run(self, lines):
        new_lines = [];
        for line in lines :
            m = CODE_RE.match(line)
            if m:
                filein = m.group('src')
                for line in codecs.open(filein, 'r', encoding="utf-8"):
                    new_lines.append('    ' + line.rstrip())
            else :
                new_lines.append(line)
        return new_lines


class CodeExtension(Extension):
# Déclaration de mon extension
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('code', CodePreprocessor(md),'>reference')

def makeExtension(configs=None):
    return CodeExtension(configs=configs)
