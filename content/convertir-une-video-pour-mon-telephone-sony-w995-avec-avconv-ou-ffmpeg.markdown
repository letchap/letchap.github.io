Title: Convertir une video pour mon téléphone Sony W995 avec avconv (ou ffmpeg)
Date: 2013-02-23 21:25
Category: Shell
Tags: arista, avconv, bash, ffmpeg, Shell, w995, winff
Slug: convertir-une-video-pour-mon-telephone-sony-w995-avec-avconv-ou-ffmpeg

Convertir des videos ou de fichiers audios sur Mac OS X pour un vieux téléphone comme le mien, c’est assez fastidieux. Il faut obligatoirement passer par itunes et par le logiciel de synchronisation tout moche disponible sur le site du fabricant.

Sur Lubuntu, pas d’itunes et pas de logiciel de synchronisation. Alors, comment convertir ces maudits fichiers ?

### 1ère tentative avortée : trouver des logiciels de conversion

Personnellement j’ai testé deux logiciels : Arista et WINFF (disponibles dans la logithèque Lubuntu ou les paquets synaptic).

#### Arista

Le plus beau graphiquement, le problème vient du fait que la présélection pour le W995 disponible sur leur site ne fonctionne pas (une présélection est un jeu de paramètres de conversion de fichiers, spécifique à un appareil ou à une famille d’appareil).

Mais c’est beau et ça fonctionne sans doute avec d’autres téléphones.

#### WINFF

Sur WINFF, il faut créer soit même sa présélection pour le W995, car elle n’est pas disponible par défaut. Et pour créer soit même sa présélection, finalement, il faut déjà faire tout le boulot de recherche et de paramétrage de la conversion soi-même, en résumé, il faut trouver tout seul comment fonctionne les commandes avconv ou ffmpeg, donc pas besoin de WINFF. D’autant plus que pour le coup, WINFF c’est moche et pas très convivial.

En revanche, grâce à WINFF, je me suis posé les bonnes questions pour arriver à la solution. Et WINFF fonctionne sans doute très bien avec d’autres téléphones.

### 2ème tentative : avec une ligne de commande : avconv ou ffmpeg

Ce que je décris ici fonctionne indifféremment avec la commande avconv ou ffmpeg. Vous pouvez remplacer l’une par l’autre. Après, comme je ne comprends rien au débat autour de ces deux commandes, je ne me suis pas posé plus de questions que ça.

#### 1. Quels sont les caractéristiques du format de sortie ?

Avant de convertir, il faut savoir en quoi convertir. Nous allons trouver l’information sur la documentation utilisateur de l’appareil.

La taille de l’image, c’est 320x240, le format video mpeg4, le format audio AAC. A priori, ces informations sont largement suffisantes.

#### 2. comment fonctionne avconv ou ffmpeg ?

Le programme avconv s'installe avec le paquet libav-tools

Voici la ligne de commande brute de décoffrage :

    :::bash
	$ avconv -i monfichier.avi -c:a aac -strict experimental -b:a 128k -ar 44100 -c:v mpeg4 -b:v 600k -s 320x240 ~/vidéos/monfichier.mp4

Dans le détail :

- Avconv : la commande de conversion (le fonctionnement est le même en mettant ffmpeg à la place de avconv),
- -i monfichier.avi : le fichier d’entrée,
- -c:v mpeg4 –b:v 600k : j’utilise pour convertir la partie video le codec mpeg 4 avec une qualité de conversion de 600k (c'est largement suffisant pour mon téléphone)
- -c:a -strict experimental -b:a 128k -ar 44100 : j’utilise pour convertir la partie son le codec aac livré par défaut sur avconv. Pour cela, il faut ajouter `-strict experimental` sinon avconv fait apparaître un message d'avertissement. Il est possible d'utiliser d'autres librairies comme libvo-aacenc ou libfaac. Elles ne sont pas installées par défaut, et dans certains cas il faudra recompiler avconv (sur Debian, pas sur Mageia par exemple).
- ~/Video/monfichier.mp4 : le fichier de sortie, ici dans le dossier video de mon répertoire personnel.

Pour connaître la liste des formats disponibles sur votre version d'avconv vous pouvez taper la commande suivante dans le terminal :

    :::bash
	$ avconv -formats


# 3ème tentative : mon premier script en shell

C’est bien beau cette ligne de commande, mais ça reste quand même moins convivial que WINFF.

Je me suis donc lancé dans l’écriture de mon tout premier script en shell pour automatiser tout ça.

J’ai donc besoin de convertir toute une série de fichiers video dans des formats différents sans être obligé de lancer une ligne de commande par fichier en changeant à chaque fois à la main le fichier en entrée et le fichier en sortie.

Le script le voici (à créer dans un fichier monscript.sh)

	#!/bin/bash
	for file in *.avi *.mp4; do
	avconv -i $file -c:a aac -strict experimental -b:a 128k -ar 44100 -c:v mpeg4 -b:v 600k -s 320x240 ~/Video/"${file%%.*}.mp4"
	done

Ce que je trouve beau, c’est qu’une automatisation de tâche tienne en 4 lignes de code, et encore, comme c’est mon premier script, je suis sûr qu’un pro ferait beaucoup mieux.

Pour expliquer un peu ce qui se passe là-dedans :

La 1ère ligne permet tout simplement de dire qu’on est en train d’écrire un script shell, et qu’on utilisera l’interpréteur bash.

La 2ème ligne initialise une variable appelée file avec différents types de fichiers video. Ici, file va prendre successivement les valeurs *.avi, puis *.mp4. Enfin, pour chacun de ses fichiers (for) il va lancer la commande de la 3ème ligne (do).

La 3ème ligne va lancer successivement la conversion de tous les fichiers .avi et .mp4 qu’il trouvera dans le répertoire où est lancé le programme. Nous reconnaîtrons au passage la ligne de commande du §2 avec quelques petites différences.

-i : nous passons la variable file en paramètre en écrivant $file.

~/Video/"${file%%.*}.mp4" : Le fichier de sortie : je le renomme en .mp4 en modifiant l’extension grâce aux outils de traitement de variable %%. Pour plus d’explication, il faut trouver un manuel shell qui explique ce que sont les outils de traitements. Sinon, vous pouvez copier le script tel quel, il est testé et approuvé.

La 4ème ligne, va clore la boucle initiée par "for".

Derniers éléments d’informations si vous souhaitez vous lancer dans l’écriture d’un script :

- il faut changer les droits du script pour le rendre exécutable : chmod +x monscript.sh
- il se lance de la manière suivante (attention aux chemins des répertoires où se trouvent les fichiers et le programme, nous verrons plus tard comment simplifier les lancements):
	
		:::bash
		$ ./monscript.sh

Du coup, j’en ai profité pour faire un autre script pour les fichiers audio sur le même principe pour transformer des fichiers flac en m4a, en n’utilisant que la partie –c:a, sans la partie -c:v. Et comme j’en ai aussi profité pour approfondir mes connaissances shell, le prochain billet parlera variables, sed, expressions régulières, tubes, que du bonheur.

