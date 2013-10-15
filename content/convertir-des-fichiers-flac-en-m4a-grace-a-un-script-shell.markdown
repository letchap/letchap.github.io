Title: Convertir des fichiers flac en m4a grâce à un script shell
Date: 2013-02-23 21:36
Category: Shell
Tags: Linux, Lubuntu, Shell, Python
Slug: convertir-des-fichiers-flac-en-m4a-grace-a-un-script-shell

Dans le précédent billet, nous avons vu comment convertir une video grâce aux commandes avconv et ffmpeg et comment l’automatiser dans un script shell.

Cette fois ci, nous allons faire la même chose pour convertir des fichiers audio flac en m4a en introduisant deux contraintes supplémentaires :

- Lancer le programme depuis n’importe quel endroit
- Copier le dossier d’origine contenant les fichiers audios à convertir dans le répertoire musique avec les fichiers convertis.


C’est parti, voici le code :
	
	#!bash
	#!/bin/bash
	for file in $(find ~ -type f -name "*.flac"); do
	rep=$(printf $file | sed –re "s/^[[:punct:][:alnum:]]+\/([[:alnum:]]+)\/[[:alnum:]]+\.flac/\1/")
	titre=$(echo $file)
	if [ ! -d ~/Musique/$rep ]; then
	mkdir ~/Musique/$rep
	fi
	avconv -i $file -acodec libvo_aacenc -ab 192k -ar 44100 ~/Musique/"$rep"/"${titre%%.flac}.m4a"
	done


Nous allons décortiquer tout ça et expliquer les éléments mis en œuvre dans ce script.

Le principe général:

- Je recherche dans mon dossier personnel tous les fichiers flac,
- Je cherche le dossier dans lequel sont rangés ces fichiers, dossier qui est en général un nom d’album,
- Je créé le dossier dans le répertoire musique,
- Je convertis mes fichiers audio et je les range dans le bon dossier du répertoire musique.

La première ligne indique que nous sommes en train d’écrire un script shell avec un interpréteur bash.

La 2ème ligne introduit deux notions : les boucles et la substitution :

- Nous alimentons une variable file avec le résultat de la commande find. La synthaxe est la suivante $(commande),
- La commande find en elle-même va rechercher tous les fichiers (type –f) dont le nom (-name) se termine par l’extension *.flac sur l’ensemble des répertoires et sous répertoires de l’utilisateur (~),
- La variable file va prendre successivement comme valeur le contenu de la commande file et pour chacune de ces valeurs va effectuer le traitement (for file in $(); do).

Sur la 3ème ligne nous allons récupérer dans une variable rep le nom du répertoire dans lequel se trouve le fichier flac, ce répertoire porte en général le nom de l’artiste ou de l’album, cela permet de classer les fichiers une fois convertis. Pour cela nous allons utiliser un tube et la commande sed et les expressions régulière

Commençons par la fin, la commande sed. La commande sed permet de rechercher et de remplacer des caractères dans une chaîne de caractères. Cela se fait au moyen des expressions régulières

`^[[:punct:][:alnum:]]+\/([[:alnum:]]+)\/[[:alnum:]]+.flac` signifie :

Je commence par le début de ma chaîne, je cherche une série de caractères de ponctuation ou aplhanumérique jusqu’à sélectionner une série de caractères aplhanumériques encadrer par deux "/" se trouvant avant le nom du fichier se finissant par ".flac"

Ici les anti-slash sont des caractères d’échappement du "/" et du "." qui peuvent être confondus avec des expressions régulières.

Entre les "()" se trouvent ce que l’on veut extraire.

Ceci est un petit exemple d’utilisation des expressions régulières. Elles sont évidemment beaucoup plus riches que ce qui est présenté ici, n’hésitez pas à vous plongez dedans et faire vos propres tests.

Enfin dans le reste de la commande sed –r siginifie que nous utilisons les expressions régulières étendues, -e que les instructions sed se trouvent directement dans la ligne de commande et non pas dans un fichier, et s/xxx/\1/ que nous faisons une recherche dont nous stockons le résultat dans 1.

Ouf !

Mais comment passer le contenu de la variable file à sed pour alimenter la variable rep. Grâce à un printf de la variable file dont nous redirigeons la sortie grâce à un tube | vers la commande sed.

En 4ème ligne, nous récupérons le titre de la chanson dans une variable titre par un simple echo $file.

Sur la 5ème ligne, nous allons tester si le dossier contenant nos titres existe déjà dans le répertoire Musique grâce au test `[ ! –d xxx]`. [ ] veut dire que nous faisons un test, ! teste la non existence et –d indique que nous faisons un test sur un nom de répertoire.

Si le répertoire n’existe pas, alors nous le créons par la commande mkdir en ligne 6.

Fin de la boucle si en ligne 7 par un fi.

Nous avons déjà vu la conversion en ligne 8 dans un précédent article, je n’y reviens pas (j’ai simplement supprimer la partie –vcodec) , ainsi que le bouclage de la boucle for par le petit done de la ligne 9.

Et voilà, c'est prêt pour une conversion.

