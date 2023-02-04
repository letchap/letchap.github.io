Title: Envoyer une notification utilisateur à partir d'une commande root
Date: 2014-01-06 22:36
Category: Shell
Tags: shell, terminal, slim, crunchbang, xauth
Slug: envoyer-une-notification-utilisateur-a-partir-d-une-commande-root

Vous allez me dire, à quoi ça sert ? On ne devrait jamais se connecter en root ! C'est dangereux et cela signifie que les droits sont mal gérés. Si je veux envoyer une notification utilisateur, je lance la commande en tant qu'utilisateur, un point c'est tout. Malheureusement, cela ne fonctionne pas avec anacron qui ne s'exécute qu'en root, à moins de créer une instance non root spécialement [ce que je détaille ici]({filename}/lancer-anacron-comme-simple-utilisateur.markdown). Et là patatras, un job lancé par anacron en root n'enverra jamais de message sur une session utilisateur.

Pour la suite de l'article, il faut avoir en tête qu'à chaque utilisateur est associé une session du serveur X qui gère notammenent l'interface graphique. Par défaut, le root n'a pas le droit de se connecter au serveur X d'un utilisateur non-root.

Heureusement, il est possible de forcer un job lancé en root à envoyer un message sur une session du serveur X. Pour cela nous allons modifier la variable d'environnement DISPLAY du root que nous allons fusionner avec celle de l'utilisateur le temps de l'exécution de la commande.

La variable d'environnement DISPLAY contient les éléments suivants :
    `machine:numéro_display.numéro_écran`

Pour un simple utilisateur comme moi, pas de nom de machine, un seul écran, elle va donc s'afficher avec `:0.0`

Maintenant, comment rappatrier l'authentification au serveur X de l'utilisateur et le passer au root : en utilisant la commande `xauth`. `xauth` est utilisé pour éditer et fournir les authorisations d'un serveur X. Associé à la commande `merge`, elle va permettre de récupérer les authorisations de l'utilisateur et les passer au root.

Enfin, pour ne faire cette opération que le temps de l'exécution de la commande, nous allons utiliser la commande `env` qui permet justement de définir une variable le temps de la commande.

Un dernier point avant d'afficher la solution. Mais où récupère t-on les authorisations de l'utlisateur ?

Pour cela, il faut connaître son gestionnaire d'affichage, ou Display Manager dans la langue de Stallman. Les plus connus sont gdm ou kdm. Bon sur Crunchbang, c'est slim (sur Archlinux aussi d'ailleurs). Pour s'en assurer, il suffit de faire :

    :::bash
    $ cat /etc/X11/default-display-manager
    /usr/bin/slim

Les informations qui nous intéressent vont se trouver dans le fichier `/etc/slim.conf`.

    :::bash
    $ cat /etc/slim.conf
    # Xauth file for server
    authfile           /var/run/slim.auth

Voilà, les authorisations de l'utilisateur se trouvent dans le fichier `/var/run/slim.auth`.

Il ne reste plus qu'à compiler tout ça, et la solution est :

    :::bash
    $ sudo env DISPLAY=:0 xauth merge /var/run/slim.auth & ma_commande



