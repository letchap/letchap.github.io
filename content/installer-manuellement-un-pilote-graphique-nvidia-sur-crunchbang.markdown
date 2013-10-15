Title: Installer manuellement un pilote graphique Nvidia sur Crunchbang
Date: 2013-06-05 22:02
Category: Crunchbang
Tags: Crunchbang, Nvidia, Terminal
Slug: installer-manuellement-un-pilote-graphique-nvidia-sur-crunchbang

La distribution Crunchbang est une distribution trés légére basée sur Debian. Lors de l'installation sur mon vieux PC, la partie inférieure de l'écran est inutilisable car la carte graphique est mal gérée. Il faut alors installer le pilote graphique propriétaire, Nvidia dans mon cas. Crunchbang, se voulant trés léger, il n'y a pas par défaut d'interface graphique pour installer le pilote, nous allons donc l'installer via le terminal.

Ce post est très largement inspiré du wiki Debian disponible [à cette adresse](http://wiki.debian.org/NvidiaGraphicsDrivers#NVIDIA_Proprietary_Driver "wiki Debian")

### Quel pilote ?

La première étape consiste à savoir quel pilote installer en fonction de sa carte graphique. Pour connaître les caractéristiques de votre matériel sur Crunchbang, vous pouvez installer l'utilitaire hardinfo :
    
	:::bash
	$ sudo apt-get install hardinfo

Dans mon cas, il s'agit d'une carte Nvidia Geforce 5200
![Hardinfo]({filename}/images/hardinfo.png "Hardinfo")

Ensuite, il suffit d'aller sur le [site de nvidia](http://www.nvidia.fr/Download/Find.aspx?lang=fr "Choix du pilote Nvidia") et de choisir la carte, et le site renvoie le nom du pilote à utiliser. Dans mon cas toujours le 173.
![Nvidia]({filename}/images/nvidia.png "Résultat de la recherche du pilote")

### Puis - je installer des pilotes non-libres ?

La deuxième étape consiste à vérifier que nous pouvons installer des paquets non-libres. Par défaut, sur Crunchbang Waldorf, c'est le cas. Pour s'en assurer, il suffit de vérifier la présence de "non-free" dans la liste des sources. La commande :

	:::bash
    $ cat /etc/apt/sources.list

devrait vous renvoyer :

	## DEBIAN
    deb http://http.debian.net/debian/ wheezy main contrib non-free

S'il n'est pas présent, ajouter ces deux lignes en éditant le fichier :

	:::bash
    $ sudo nano /etc/apt/sources.list

### J'installe mon pilote

Le pilote s'installe avec les deux commandes suivantes dans le terminal :

	:::bash
    $ sudo apt-get update
    $ sudo apt-get -r install linux-headers-$(uname -r|sed 's,[^-]*-[^-]*-,,') nvidia-kernel-legacy-173xx-dkms

### Mon pilote n'est pas détecté par défaut

La dernière étape consiste à faire reconnaître le pilote par le système, qui n'est pas détecté automatiquement par défaut. Pour cela, il faut créer un fichier de configuration :

	:::bash
    $ sudo nano /etc/X11/xorg.conf.d/20-nvidia.conf

et ajouter les lignes suivantes :

    Section "Device"
        Identifier     "Mon pilote graphique"
        Driver         "Nvidia"
    EndSection

C'est fini, il ne reste plus qu'à redémarrer.
