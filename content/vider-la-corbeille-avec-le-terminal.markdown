Title: Vider la corbeille avec le terminal
Date: 2013-02-25 22:18
Category: Shell
Tags: Corbeille, Linux, Lubuntu, Terminal
Slug: vider-la-corbeille-avec-le-terminal

Avec mon Lubuntu 12.04, j'ai parfois des soucis avec la corbeille : je ne vois pas les fichiers à supprimer, et donc je ne peux pas vider la corbeille. Il m'arrive parfois des messages d'erreur.

Je suis alors obligé de vider la corbeille via le terminal et comme je ne me souviens jamais de l'emplacement, je me le note, ainsi que les commandes de suppression :

	:::bash
    $ cd ~/.local/share/Trash/
    $ rm -rf files 
    $ rm -rf info 
    $ rm -rf expunged

Voilà, une corbeille comme neuve.
