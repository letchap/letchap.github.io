Title: Créer un fichier pdf avec Python et Reportlab
Date: 2014-03-06 21:36
Category: Python
Tags: Python, Reportlab, pyfpdf
Slug: creer-un-fichier-pdf-avec-python-et-reportlab

Dans un billet précédent, pour créer un document pdf, [j'avais utilisé la bibliothèque tierce pyfpdf]({filename}/transformer-un-texte-chinois-en-pdf.markdown). Si cette bibliothèque s'avère extrèmement facile à prendre en main pour créer un fichier pdf à partir d'un fichier texte, elle présente à l'utilisation deux inconvénients majeures :

- la création d'une document d'une centaine de page est très longs, plusieurs minutes
- pour une raison que je ne m'explique pas, la conversion de certains caractères chinois est incorrecte au moment de la création du fichier pdf.

Il me fallait donc trouver une autre solution.

J'avais bien repéré la bibliothèque Reportlab pour Python, qui est la bibliothque de référence pour la création de fichier pdf. Mais comme je n'avais pas obtenu de résultats probants aussi rapidement qu'avec pyfpdf, je l'avais mis de coté. Grave erreur.

C'est de la faute à la doc reportlab aussi. Je dois transformer du texte en pdf et je vois un chapître entièrement consacrer à la transformation de texte en pdf. Chouette, je vais utiliser cette fonctionalité : "text objet method". Et bien, surtout pas. Il faut se prendre la tête à positionner un curseur, il n'y a pas nativement de multipage, la mise en page est inexistante. Une galère.

En revanche, il y a une fonctionnalité géniale, PLATYPUS : Page Layout and Typography Using Scripts. Et là, ça déchire.

Comme un petit script vaut mieux qu'un long discours, voyons comment créer un fichier pdf à partir d'un fichier texte avec reportlab :

    #!python
    import sys

    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.styles import ParagraphStyle

    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

    def pdf(filein):
        txt = open(filein, 'r').read()
        docpdf = SimpleDocTemplate(fileout, 
                                   pagesize = A4)
        style = getSampleStyleSheet()
        style.add(ParagraphStyle(name='Chinese',
                                 fontName='STSong-Light',
                                 fontSize=12,
                                 leading=14),
                                 wordWrap = 'CJK')

        story = []
        paragraphs = txt.split("\n")
        for para in paragraphs:
            story.append(Paragraph(para, style["Chinese"]))
            story.append(Spacer(0, cm * .3))
        docpdf.build(story)

    if __name__ == '__main__':
        if len(sys.argv) < 3:
            print('Utilisation : <script> textfile pdffile')
            sys.exit(1)
        else :
            filein = sys.argv[1]
            fileout = sys.argv[2]
            pdf(filein)
            
            
            

Commençons par les imports :

- l'import de sys est uniquement pour gérer les fichiers d'entrée et de sortie
- ensuite, nous importons diférents modules de reportlab pour gérer le format de la feuille, et l'unité de mesure
- puis, nous importons l'ensemble des modules de PLATYPUS qui vont nous permettre de gérer le style du document et des paragraphes
- enfin le dernier bloc d'import sert à gérer une police unicode pour les caractères chinois.


Concernant le code lui-même :

- en ligne 15, nous ouvrons le fichier en lecture
- puis en ligne 16 nous définissons les caractéristiques de notre document
- en ligne 18 à 23 nous créons un style auquel nous apportons des caractéristiques particulières comme la police, la taille de la police, et surtout, le plus important pour l'écriture chinoise, un flag 'CJK' pour les ruptures en bout de ligne. Sans cela, la ligne dépasserait le cadre de la page. Toutes les possibilités de paramétrages du style sont décrites dans la documentation reportlab disponible [à cette adresse](http://www.reportlab.com/docs/reportlab-userguide.pdf "reportlab").
- Par défaut, le multi-pages est géré.
- à partir de la ligne 25 et jusqu'à la ligne 30, nous lisons ligne à ligne notre texte et nous alimentons une liste, liste qui sera à son tour lue pour constituer le document pdf en applicant le style défini plus haut.

Par rapport à pyfpdf, je n'ai plus de problème de changement intempestif de caractères chinois et surtout, cela va beaucoup, beaucoup plus vite. Quelques secondes pour un fichier d'une centaine de pages.

Moralité, il ne faut pas refuser l'obstacle, la satisfaction est au bout de l'effort.