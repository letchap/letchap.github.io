#!/usr/bin/python
# -*- coding: utf8 -*-
#---------------------
#newpost.py
#Cree par letchap
#---------------------

import re
import sys
import os
from unidecode import unidecode
import time

def slugify(titre):

    # je m'assure d'avoir de l'unicode
    value = titre.decode('utf8')
    # je transforme mon texte en ascii
    value = unidecode(value)
    # je supprime les caractères spéciaux, je normalise les espaces, je mets en minuscule
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    # je rajoute les tirets et je renvoie le titre slugifié
    return re.sub('[-\s]+', '-', value)

def newpost(titre):

    slug = slugify(titre)

    if os.path.isfile(os.path.join(os.getcwd(), "content/" + str(slug) + ".markdown")):
        print('Ce fichier existe déjà') # bon, comme son nom l'indique, c'est pour tester les doublons
        sys.exit(1)
    else:   
		with open(os.path.join(os.getcwd(), "content/" + str(slug) + ".markdown"), "w") as f: # si je n'ai pas de doublon, je crée le fichier et le squelette de mon post dans content
			f.write("Title: " + titre + "\n")
			f.write("Date: " + time.strftime('%Y-%m-%d %H:%M', time.localtime()) + "\n")
			f.write("Category: " + "\n")
			f.write("Tags: " + "\n")
			f.write("Slug: " + slug +"\n\n")



if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Précisez le titre du post')
		sys.exit(1)
	else:
		titre = sys.argv[1]
		newpost(titre)
