#!/usr/bin/python
# -*- coding: utf8 -*-
#---------------------
#txt2pdf.py
#Crée par letchap
#---------------------

import sys
import chardet
from fpdf import FPDF
import os

def decodage(filename):

	# Je cherche l'encodage de mon fichier grâce à chardet
	rawdata = open(filename, 'r').read(100)
	codage = chardet.detect(rawdata)
	source = codage['encoding']

	# Je prépare mon PDF, j'utilise pyfpdf
	pdf=FPDF('P','pt','A4')
	pdf.add_page()
	# J'utlise une jolie police de caractère dont je doit indiqué le chemin (sur Mac OSX)
	pdf.add_font('fireflysung', '', '/Library/Fonts/fireflysung.ttf', uni=True)
	pdf.set_font('fireflysung','', 12)
	# Je décode et j'encode mon texte
	txt=file(filename).read().decode(source, errors='ignore').encode('utf8')
	pdf.write(14, txt)
	# Je retravaille le nom du fichier
	ext=os.path.basename(filename) # j'enlève le chemin
	namefile=os.path.splitext(ext)[0] # j'enlève l'extension
	# Je finalise le pdf
	pdf.output('/path/to/new_' + namefile + '.pdf','F')


#############################################################################################
#                           Le main                                                         #
#############################################################################################
# Je teste le nombre d'arguments de la ligne de commande
# 0 = premier paramètre, le nom du programme
# 1 = deuxième paramètre, ici le nom du fichier.
# Si j'ai strictement moins de 2 paramètres, j'ai oublié le nom de fichier
# Je sors alors en erreur sys.exit(1), (0 pas d'erreur, 2 erreur de synthaxe de la ligne de commande)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Précisez le fichier à décoder')
		sys.exit(1)
	else :
		filename = sys.argv[1]
		decodage(filename)
		



