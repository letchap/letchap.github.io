Title: Connexion ssh avec VirtualBox
Date: 2014-03-20 22:03
Category: VirtualBox
Tags: VirtualBox, SSH, Crunchbang
Slug: connexion-ssh-avec-virtualbox

En conservant le paramétrage par défaut de VirtualBox, il n'est pas possible de créer une connection SSH avec un invité Linux.

Pour rendre possible cette connection SSH, il faut modifier le paramétrage de l'onglet réseau dans VirtualBox pour le positionner sur "Accès par pont". Cela vous permettra d'avoir une adresse au format 192.168.0.xx.

Pour rappel sur Linux, vous aurez auparavant installé openssh et démarré le service par `service ssh start`.

N'oublier de préciser de port 22 lors de votre connection SFTP.
