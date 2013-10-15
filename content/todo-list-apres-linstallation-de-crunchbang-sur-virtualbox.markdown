Title: ToDo list après l'installation de Crunchbang sur VirtualBox
Date: 2013-06-07 23:32
Category: VirtualBox
Tags: Crunchbang, VirtualBox, Terminal, Guest Additions, dkms, 
Slug: todo-list-apres-linstallation-de-crunchbang-sur-virtualbox

J'ai testé un certain nombre de distributions sur une VirtualBox installée sur un iMac et la plus stable à ce jour est sans conteste Crunchbang. De plus, comme c'est une distribution légère, j'ai l'impression d'avoir une bête de course. Mais surtout, surtout, fini les problèmes d'affichage, les redémarrages douloureux après une mise à jour. Les releases stables, ça a du bon.

J'ai déjà eu l'occasion de décrire la procédure d'installation d'une distribution sur VirtualBox [dans un billet précédent]({filename}/virtualiser-mageia-2-sur-os-x-mountain-lion-avec-virtualbox.markdown "Virtualiser"), nous allons nous attarder dans ce billet sur les compléments d'installation qui rendent l'utilisation de la VirtualBox plus agréable. Crunchbang étant par nature assez chichement doté en outils graphiques, ces petits compléments se feront par le terminal. Quand les commandes sont connues, ce n'est pas plus long que par des outils graphiques, bien au contraire.

### Installation de VirtualBox Guest Additions

Les Guest Additions permettent notamment l'affichage en plein écran.

Tout d'abord :

	:::bash
    $ sudo apt-get install build-essential linux-headers-`uname -r` dkms

Les Guest Additions se trouvent dans une image disque virtuelle que nous montons en sélectionnant "Installer les Guest Additions" dans le menu Devices (périphérique) de VirtualBox

Le disque devrait apparaître dans le gestionnaire de fichier, dans mon cas il est monté sur /media/cdrom0

Il ne reste plus qu'à lancer la procédure d'installation :

    :::bash
	$ sudo sh /media/cdrom0/VBoxLinuxAdditions.run


### Dossier partage

Un deuxième gros intérêt des Guest Additions est la possibilité de partager des fichiers entre le système hôte et le système invité. Après avoir créer un dossier partage sur le système hôte, par défaut, il se retrouvere dans le répertoire Media (dossier commençant par "sf_") de votre Crunchbang virtualisé mais ne sera pas accessible à l'utilisateur. Pour donner les droits d'accès à ce dossier, il faut ajouter l'utilisateur au groupe Vbox.

Pour cela, il faut éditer le fichier /etc/groups, repérer la ligne commençant par vboxsf et ajouter son nom de user, par exemple :

    vboxsf:x:1001:letchap

### Modification du clavier

La procédure d'installation de Crunchbang ne permet pas de choisir le clavier. Par défaut, il installe un clavier azerty "classique". Je n'ai donc pas eu la possibilité de paramétrer le clavier Mac. Ce qui pose quelques petits problèmes quand je veux taper "-" par exemple, ou des crochets.

Il est possible de changer la configuration du clavier à partir du terminal, pour cela il faut éditer les fichier /etc/default/keyboard et le renseigner de la manière suivante :

    XKBMODEL="pc105"
    XKBLAYOUT="fr"
    XKBVARIANT="mac"
    XKBOPTIONS=""
    

Il ne reste plus qu'à redémarrer la machine virtuelle pour bénéficier de tous ces ajouts.


