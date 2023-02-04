Title: Programmer des travaux avec Automator et iCal
Date: 2013-12-19 20:54
Category: Mac OS X
Tags: Mac OS X, Mavericks, Python, Automator, iCal, notification center
Slug: programmer-des-travaux-avec-automator-et-ical

Il y a toujours plusieurs façons de faire.

Il y a quelques mois, nous avons vu comment programmer de manière périodique, sur Mac OS X, [l'exécution d'un programme Python avec launchd]({filename}/demarrage-automatique-de-travaux-avec-launchd.markdown), ce programme Python envoyant alors [une notification au centre de notification grâce à un décorateur]({filename}/envoyer-une-notification-au-centre-de-notification-de-mountain-lion-avec-python.markdown).

Et bien, tout ça ne sert à rien. Dans OS X Mavericks, la programmation périodique et l'envoi d'une notification peut se gérer grâce à Automator. Nous repartons de notre programme Python dans lequel nous enlevons tout ce qui concerne l'envoi d'une notification. Et voici comment programmer le tout :

### Création d'un workflow calendrier dans iCal

Nous lançons Automator en choisissant "Alarme Calendrier"

[![Automator]({static}/images/ical/automator.png "Automator")]({static}/images/ical/automator.png){: data-lightbox="automator" title="Automator" }


### Création d'un workflow Automator

Puis, nous définissons notre processus Automator avec l'execution d'un programme Ptyhon à partir du termenial et l'envoi d'une notification.

[![Shell]({static}/images/ical/shell.png "Automator")]({static}/images/ical/shell.png){: data-lightbox="automator" title="Workflow Automator" }

### Sauvegarde du workflow

Nous enregistrons le processus qui va s'inscrire dans iCal.

[![Save]({static}/images/ical/save.png "Save")]({static}/images/ical/save.png){: data-lightbox="automator" title="Sauvegarde du Workflow" }

### Dans iCal

Il ne reste plus qu'à programmer sa périodicité.

[![iCal]({static}/images/ical/ical.png "iCal")]({static}/images/ical/ical.png){: data-lightbox="automator" title="iCal" }

[![Périodicité]({static}/images/ical/periode.png "Périodicité")]({static}/images/ical/periode.png){: data-lightbox="automator" title="Périodicité" }

C'est plus simple, mais évidemment, beaucoup moins fun que de tout faire à la main.