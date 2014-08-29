Title: Transformer un texte chinois en pdf
Date: 2013-11-25 17:05
Category: Python
Tags: UTF8, decodage, encodage, GB2312, BIG5, python, chardet, pyfpdf
Slug: transformer-un-texte-chinois-en-pdf

Nous sommes tous confrontés un jour au problème de l'encodage, aka "c'est quoi tous ces hiéroglyphes bizarres dans mon document au lieu de mon beau texte en chinois (ou en suédois, en russe, en arabe, ou même en français....)?"

Bon, je ne vais pas faire un cours sur l'encodage, sachez juste que si vous avez des hiéroglyphes, que vous êtes sur Mac ou Linux, il y a des fortes chances que votre document ne soit pas en unicode mais dans un encodage régional, comme par exemple pour un texte chinois GB2312 (chinois simplifié) ou BIG5 (chinois traditionnel).

Qu'à cela ne tienne, nous allons convertir notre texte dans un format unicode universel, dans sa version UTF8. Et puis, pour pouvoir lire le texte en toute circonstance et sur toute plateforme, nous allons en faire un pdf

Pour cela, nous allons utiliser deux bibliothèques tierces de Python, chardet qui permet de deviner l'encodage de notre fichier texte de départ (très pratique si nous ne le connaissons pas) et pyfpdf qui permet de créer un fichier pdf (plus simple à utiliser que reportlab). Les deux bibliothèques s'installent avec pip. la documentation pyfpdf est [ici](http://code.google.com/p/pyfpdf/).

Allez, le programme python. Les commentaires sont dans le code.

{% code content/code/txt2pdf.py %}
[Télécharger txt2pdf.py]({filename}/code/txt2pdf.py){: class="button radius tiny" title="Télécharger txt2pdf.py" }

Voilà, il n'y a plus qu'à lancer le programme par un beau

	$ ./txt2pdf.py montexte.txt

Evidemment, pour tout être normalement constitué, lancer un décodage de cette manière, en ligne de commande, ce n'est pas très pratique, un clic droit sur un ou plusieurs fichiers serait le bienvenue. C'est que nous allons faire tout de suite [dans ce billet]({filename}/lancer-un-programme-python-depuis-automator.markdown)
