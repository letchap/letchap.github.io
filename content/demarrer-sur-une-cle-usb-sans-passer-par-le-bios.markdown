Title: Démarrer sur une clé USB sans passer par le BIOS
Date: 2013-02-23 21:16
Category: Linux
Tags: BIOS, Boot, Grub, Grub2, Installation, Lubuntu, Plop Manager
Slug: demarrer-sur-une-cle-usb-sans-passer-par-le-bios

Faire des clés live USB c’est bien joli, mais si on ne peut pas démarrer sur une clé USB sur son ordinosaure, c’est ballot.

Heureusement, il existe une solution pour démarrer sur une clé USB sans passer par le BIOS : Plop Manager.

Si vous souhaitez vous lancer, je vous mets en garde, c’est assez difficile. Nous allons essayer d’y aller pas à pas.

Tout d’abord, le principe général :

Sur Ubuntu, le gestionnaire de démarrage s’appelle GRUB. Par défaut, il se contente de lancer le système d’exploitation. Lorsqu’il y a plusieurs systèmes d’exploitation installés sur la machine (dual boot), c’est GRUB qui va vous donner le choix du système sur lequel démarrer. Nous allons ajouter une entrée dans GRUB qui lancera le programme Plop Manager au démarrage et nous permettra ainsi de démarrer sur la clé USB.

Nous allons commencer par installer Plop Manager.

Pour cela, il faut télécharger le dossier plpbt-5.0.14.zip (c’est la dernière version au moment de l’écriture du billet) sur le site de Plop manager [à cette adresse](http://www.plop.at/en/bootmanager/download.html "Plop manager").

Vous décompressez le .zip et vous copiez le fichier plpbt.bin dans le répertoire /boot.

Ensuite il faut éditer le fichier /etc/grub.d/40_custom avec `sudo nano /etc/grub.d/40_custom`, puis ajouter les lignes ci-dessous : 

    menuentry "Plop Boot Manager" {
    set root='(hd0,1)'
    linux16 /boot/plpbt.bin
    }

Comme son nom l'indique, il s'agit d'un fichier où nous pouvons ajouter des entrées personnalisées dans GRUB.

Nous avons maintenant installé le programme et ajouté une entrée pour appeler ce programme dans GRUB.

Dernière étape sur certaines distrubutions (Ubuntu par exemple), il faut forcer l'affichage du GRUB au démarrage. En effet, si certaines distributions proposent l'affichage systématique de GRUB par défaut, d'autres non et lancent directement le système présent sur l'ordinateur s'il est le seul présent.

IL est possible de modifier ce paramètrage de deux manières. D'abord avec l'outil graphique GRUB Customizer disponible dans un ppa en tapant les commandes suivantes dans le terminal :

	:::bash
    $ sudo add-apt-repository ppa:danielrichter2007/grub-customizer
    $ sudo apt-get update
    $ sudo apt-get install grub-customizer


Il est possible également de le faire manuellement en éditant le fichier /etc/default/grub en fixant une valeur de 10s par exemple pour le TIMEOUT `GRUB_TIMEOUT=10, ce qui forcera l'affichage de GRUB au démarrage.

Très important, il reste à mettre à jour GRUB avec la commande suivante dans le terminal :

    :::bash
	$ sudo update-grub

Et voilà, au démarrage, il vous sera proposé de choisir Plop Manager, puis une fois dans Plop Manager, de choisir USB pour démarrer votre PC.
