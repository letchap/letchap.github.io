Title: Récupérer la sauvegarde Time Machine sur Linux
Date: 2023-02-08 20:27
Category: Linux
Tags: Linux, Mac OS X, Time Machine
Slug: recuperer-la-sauvegarde-time-machine-sur-linux

Mon iMac ayant rendu l'âme, j'ai besoin de récupérer certaines données sauvegardées sur Time Machine pour les utiliser sur mon ordinateur tournant sous Ubuntu

J'ai trouvé un petit script qui fonctionne très bien à [cette adresse](https://gist.github.com/vjt/5183305). Le script date de 2014 mais il est toujours d'actualité. J'ai simplement ajouté une petite modification pour que le programme continue même s'il rencontre une erreur avec un 

    :::bash
    cp -van "$entry" "$dest" 2>/dev/null || :

Il suffit de lui passer en paramètre le répertoire Time Machine à récupérer (en général dans le répertoire "latest") et le répertoire de destination.

Je mets à télécharger le script modifié.

[Télécharger copy-from-time-machine.sh]({static}/code/copy-from-time-machine.sh){: class="button small" title="copy-from-time-machine.sh" }

