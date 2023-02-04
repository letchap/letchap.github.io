Title: Fabriquer une clé live usb depuis n'importe quelle distribution linux
Date: 2013-02-20 20:51
Category: Terminal
Tags: Boot, dd, df -h, isohybrid, Live USB, syslinux, terminal
Slug: fabriquer-une-cle-live-usb-depuis-nimporte-quelle-distribution-linux

J’adore tester de nouvelles distributions Linux, mais j’en ai marre de graver des tonnes de CD. La solution, la clé USB.

Il existe tout un tas de logiciels, différents selon les distributions pour créer des clés bootables. Trop compliqué pour moi. La solution qui marche sur toutes les distributions est hyper simple en 3 commandes dans le terminal : isohybrid, df – h, dd.

J’ai trouvé l’astuce [ici](http://frederic.bezies.free.fr/blog/?tag=isohybrid "Petit truc pour rendre une ISO classique démarrable sur une clé USB").

La première étape consiste à formater une clé USB. Evidemment, il faut que la clé soit suffisamment grande pour contenir le fichier .iso. Pour formater la clé USB, démarrer l’utilitaire de disque et formater la clé (en FAT32 ou EXT4, ça marche très bien).

Nous allons ensuite passé par le terminal :

Ouvrez une fenêtre de terminal

Si vous n’êtes pas familier des commandes cd pour se balader dans les répertoires à partir du terminal, vous aurez copié au préalable votre fichier .iso à la racine de votre répertoire personnel.

### 1) Isohybrid

	:::bash
    $ isohybrid image.iso


Les fichiers .iso sont plutôt destinés à être gravé sur CD, cette commande permet de copier le fichier .iso en toute sérénité sur la clé USB (de créer une version hybrid de l’image disque).

Si vous n'avez pas la commande isohybrid, il faut installer syslinux comme ceci (sous Ubuntu ou apparenté)

	:::bash
    $ sudo apt-get install syslinux


### 2) df –h

	:::bash
    $ df -h
    Sys. de fichiers Taille Utilisé Dispo Uti% Monté sur
    /dev/sda1           37G     12G   23G  35% /
    udev               241M    4,0K  241M   1% /dev
    tmpfs              100M    816K   99M   1% /run
    none               5,0M       0  5,0M   0% /run/lock
    none               248M     72K  248M   1% /run/shm
    /dev/sdb1         1004M    312M  692M  32% /media/USB


Cela permet de savoir où copier le fichier .iso. En général, cela ressemble à quelque chose comme /dev/sdb ou /dev/sdb1.

### 3) dd

Si vous n’êtes jamais entré dans le terminal, je dois vous mettre en garde, cette commande peut être dangereuse. Mal utilisée, elle peut complètement effacer votre disque dur.

Si vous avez déjà utilisé le terminal, je dois vous mettre en garde, cette commande peut être dangereuse. Mal utilisée, elle peut complètement effacer votre disque dur.

Ces précautions prises, en fait c’est très simple, il suffit de taper la commande de la manière suivante :

	:::bash
    $ sudo dd if=image.iso of=/dev/sdb


Dans le détail :

- sudo : cela signifie que nous sommes en super utilisateur, il faut donc ensuite taper son mot de passe.
- dd : c’est la commande de copie
- if : cela signifie input file, le fichier en entrée est bien le fichier .iso
- of : cela signifie output file, le fichier en sortie se trouve bien sur la clé USB. Petite astuce super importante : il faut absolument enlever le numéro de /dev/sdb1 en /dev/sdb, sinon ça ne marche pas.


Et nous voyons bien où se trouve le coté dangereux en inversant if et of, on écrase tout avec une clé vide.

Comme nous avons fait un petit coup d’isohybrid avant, pas de soucis de format au moment de la copie.

En hop, une clé bootable. Une opération que nous pouvons recommencer à l’infini. Je l'ai testée sur un très grand nombre de distributions, ça marche très bien.

