Title: De l'utilité d'un live CD pour les situations désespérées
Date: 2013-02-27 22:25
Category: Lubuntu
Tags: live CD, Lubuntu, nvidia
Slug: de-lutilite-dun-live-cd-pour-les-situations-desesperees

Catastrophe, l'écran de mon ordinateur ne fonctionne plus. C'est malin, qu'est ce qui m'a pris aussi de vouloir installer le tout dernier pilote nvidia sur mon vieux PC. Moralité, écran noir. Que faire, réinstaller mon Lubuntu ?

Bon sang mais c'est bien sûr, il faut démarrer sur CD une session live et réparer les bêtises (pour moi supprimer le pilote de la carte graphique) à partir de là.

Une fois sur la session live, il faut trouver le point de montage du disque dur. Cela peut se faire grâce à Gparted. Chez moi, c'est sur /dev/sda1.

Ensuite, il faut ouvrir le terminal et monter le disque dur, puis se positionner dessus pour pouvoir travailler.

	:::bash
    $ sudo mount /dev/sda1 /mnt
    $ sudo chroot /mnt


Le prompt va changer en #/

Ensuite je peux lancer ma commande de suppression du pilote :

	:::bash
    #/ sudo apt-get remove --purge nvidia-current


Puis je démonte le volume :

	:::bash
    #/ sudo umount /dev/sda1


Il ne reste plus qu'à redémarrer normalement.

La morale de l'histoire : avoir toujours un live CD ou une clé USB pour démarrer sous la main, ça peut sauver un ordinateur d'un propriétaire trop enthousiaste.

Cette même procédure est très utilisée pour réinstaller un Grub disparu sur la famille Ubuntu. Il y aura un petit post là-dessus bientôt.
