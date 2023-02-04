Title: J'ai dédisqusisé mon Pelican
Date: 2015-05-01 16:19
Category: Pelican
Tags: Pelican, Isso, Disqus, Openshift
Slug: jai-dedisqusise-mon-pelican



Deuxième étape dans la recherche de solutions libres autour de mon blog Pelican : remplacer le gestionnaire de commentaires Disquss par Isso.

Isso est un gestionnaire de commentaires open source et écrit en Python. Autant dire qu'il est donc parfait. Pour plus d'information vous pouvez aller voir sur le [site d'Isso](http://posativ.org/isso/ "Isso") dès maintenant mais nous allons largement y revenir.

Ma seule difficulté, comme d'habitude, est de ne pas avoir de serveur à la maison, donc, encore une fois, je vais utiliser openshift. Et là, contrairement à l'installation de piwik sur openshift qui se fait de manière très simple en 3 lignes de commandes grâce à la disponibilité d'un cartrigde piwik, pour Isso, il faut tout faire à la main.


### J'ai commencé par tatonner

Sur le site de Isso, deux procédures d'installation sont décrites : une en utilisant `pip install`, et une plus manuelle

Ma première erreur fut de croire que Isso s'installe sur Openshift comme avec un simple `pip install`. La procédure que je m'attendais à appliquer était :
    rhc app create isso python-3.3

Je mets à jour les fichiers de paramétrage wsgi.py et isso.conf comme indiqué sur le site de Isso puis :

    git add.
    git commit -m "isso my love"
    git push

Et là, comme par miracle, j'aurais eu isso installé. Que nenni, il manque les fichiers javascript `embed.min.js` et `count.min.js` indispensables pour faire tourner le client.

Pour s'en apercevoir, la commande super utile à consommer sans modération est :

    rhc app tail -a isso

qui permet de lire les logs (en particulier d'erreur) de l'application sur Openshift. Et là, on a une belle erreur `400 fichier non trouvé` sur le `GET embed.min.js`

Je n'ai pas compris pourquoi avec `pip install` en local, j'ai bien la création de mes fichiers javascript mais pas en créant l'application sur Openshift, en attendant, passage au plan B, l'installation manuelle de Isso sur openshift.



### La procédure garantie à 100% pour l'installation de Isso sur openshift est la suivante :

Je me suis largement inspiré du dépôt [commentedit](https://github.com/commentedit/commented.it/wiki/How-to-install-on-OpenShift "Commentedit")

#### Je crée une application Isso sur Openshift

Dans une fenêtre du terminal, j'entre la commande suivante :

    rhc app create isso python-3.3 --from-code https://github.com/posativ/isso.git


#### Je paramètre mon application

Je me place dans le répertoire de mon application nouvellement créée :

    cd isso

Première chose à faire, récupérer l'UUID de mon application, grâce à la commande 

    rhc app-show isso

Je crée un répertoire share et un fichier de configuration `/share/isso.conf` avec le contenu suivant :

    [general]
    dbpath = /var/lib/openshift/UUID/app-root/data/comment.db 
    host = http://letchap.github.io
    max-age = 15m
    notify = smtp
    log-file =

    [moderation]
    enabled = true
    purge-after = 30d

    [server]
    listen = http://localhost:8080
    reload = off
    profile = off

    [smtp]
    username = $username
    password = $password
    host = smtp.gmx.com
    port = 25
    security = starttls
    to = $mail
    from = $mail
    timeout = 10

    [guard]
    enabled = true
    ratelimit = 2
    direct-reply = 3
    reply-to-self = false

    [markup]
    options = strikethrough, autolink, fenced_code, no_intra_emphasis
    allowed-elements =
    allowed-attributes =

    [hash]
    salt = Eech7co8Ohloopo9Ol6baimi
    algorithm = pbkdf2

Il est important de tout renseigner, sinon il y aura des problèmes de lecture de fichier.


Puis je crée un fichier wsgi.py avec le contenu suivant :

    #!/usr/bin/python
    import os
    import site
    site.addsitedir(os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/')
    from isso import make_app, config
    application = make_app(config.load(os.environ['OPENSHIFT_REPO_DIR'] + '/share/isso.conf'))


Enfin je supprime ces quelques lignes dans .gitignore puisque je vais créer les fichiers manuellement et les pousser sur openshift :

    /isso/js/embed.min.js
    /isso/js/embed.dev.js
    /isso/js/count.min.js
    /isso/js/count.dev.js


#### Je créé mes fichiers javascript

Il faut créer les fichiers javascript `embed.min.js` et `count.min.js` manuellement avec la commande suivante :

    make init &&
    make js

En ayant préalablement installer requirejs et uglyfyjs.


#### Ne reste plus qu'à pousser

Il ne reste plus qu'à pousser le tout sur openshift 

    git add .
    git commit -m "Et c'est parti..."
    git push

### Et le client ...

Sur le client, il suffit d'ajouter ces quelques lignes 

    <script data-isso="https://commentedit-YOUR_DOMAIN.rhcloud.com/"
        src="https://isso-letchap.rhcloud.com/js/embed.min.js"></script>
    <section id="isso-thread"></section>


### L'import des données Disqus

La dernière étape est d'importer les commentaires de Disqus. Pour cela, il faut d'abord aller sur le site de Disqus et exporter les commentaires.

Après, je l'ai fait un peu brutal. Je me suis connecté en ssh sur openshift par un `rhc ssh isso` et j'ai créé un fichier disqus.xml dans le répertoire `app-root/data` et j'ai collé le contenu de mon fichier d'export.

Puis j'ai lancé la commande :

    isso -c /share/isso.conf import /app-root/data/disqus.xml

Et voilà, c'est fini. Ne reste plus qu'à supprimer son compte Disqus.

