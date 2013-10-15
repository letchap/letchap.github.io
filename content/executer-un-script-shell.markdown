Title: Exécuter un script shell
Date: 2013-02-24 22:29
Category: Shell
Tags: bash, bin, Lubuntu, $PATH, Shell
Slug: executer-un-script-shell

Nous avons fait deux beaux scripts en shell pour utiliser la commande [avconv]({filename}/convertir-des-fichiers-flac-en-m4a-grace-a-un-script-shell.markdown "Convertir des fichiers flac en m4a grâce à un script shell"). Nous avons enregistré nos scripts dans des fichiers monscript.sh. Maintenant comment exécuter ces scripts ?

La première chose à faire est de rendre exécutable le script par la commande :

	:::bash
    $ chmod +x monscript.sh

Ensuite, deux façons de lancer le script.

# Vous êtes encore en train de travailler sur votre script :

Le plus simple est de lancer le script en se plaçant dans le répertoire de travail où il se trouve et de taper la commande suivante :

    :::bash
	$ ./monscript.sh

# Vous avez fini votre joli script :

Nous pouvons placer notre script dans un des répertoires bin du système :

- dans usr/bin : le programme sera accessible à tous les utlisateurs
- dans usr/local/bin : le programme sera accessible aux utilisateurs de notre système
- dans ~/bin : le programme n'est accessible que par nous

Par bonheur, sur la version 12.04 de Lubuntu par exemple, pas besoin de modifier le PATH pour ajouter notre répertoire bin personnel. Il suffit de le créer pour qu'il soit reconnu. En effet, dans le fichier home/.profile, nous trouvons les lignes suivantes :

	:::bash
    if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
    fi

permettant de modifier automatiquement le PATH si le dossier home/bin existe.

C'est magique !

Il ne reste plus qu'à copier son script dans le répertoire ~/bin puis à le lancer depuis n'importe où en tapant son petit nom : monscript.sh

