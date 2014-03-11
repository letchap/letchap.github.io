Title: Lancer un programme python depuis automator
Date: 2013-11-26 13:41
Category: Mac OS X
Tags: Mac OS X, Mavericks, Automator, Python, shell
Slug: lancer-un-programme-python-depuis-automator

[J'ai un joli script python qui me permet de décoder un texte chinois en UTF8 tout en le tranformant en pdf]({filename}/transformer-un-texte-chinois-en-pdf.markdown). Maintenant, j'aimerais bien pouvoir le lancer d'un simple clic droit, voir même plusieurs fichiers d'un coup.

Pour cela, sur Mac OS X, il existe un utilitaire sympa, Automator. Il va nous permettre de créer un service qui lancera le traitement de notre ou de nos fichiers grâce à un clic droit.

Des éléments complémentaires sont disponibles sur le site [d'apple developper](https://developer.apple.com/library/mac/documentation/AppleApplications/Conceptual/AutomatorConcepts/Articles/ShellScriptActions.html)

Pour créer un service, je commence par choisir "service" dans automator puis, je choisis "exécuter un script Shell" 

[![Automator]({filename}/images/automator.png "Automator")]({filename}/images/automator.png){: data-lightbox="automator" title="Automator" }

A ce stade, vous avez deux possibilités : vous pouvez au choix saisir vos lignes de script python en sélectionnant /usr/bin/python dans l'interpréteur, ou alors vous pouvez préférez un script shell permettant de lancer le programme python. Je préfère nettement cette deuxième solution pour deux raisons : il n'existe qu'une seule version du programme python, et vous pouvez trapper les erreurs dans un fichier de log.

Nous saisissons donc notre script d'appel au programme python en shell, tout en oubliant pas de sélectionner "fichier ou dossier", "dans n'importe quelle application" ainsi que "comme arguments".

Pour passer le fichier d'entrée au programme python, nous utilisons la variable magique "$@".

Pour débugger le programme, il est bien sûr possible de renvoyer les sorties standard et erreur vers un fichier de log par un petit `>> log 2>&1`, ce qui peut s'avérer pratique.

Pour traiter plusieurs fichiers en entrée, il suffit de faire une petite boucle for dans le script shell.

Cerise sur le gateau, nous allons ajouter une petite notification en fin de traitement pour nous signaler que ce dernier est terminé. C'est beau.