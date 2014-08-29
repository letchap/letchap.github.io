Title: Utiliser locate sur OSX
Date: 2014-08-06 20:56
Category: Mac OS X
Tags: locate, launchctl, Mac OS X
Slug: utiliser-locate-sur-osx

J'aime bien la commande locate pour rechercher un élément sur le ou les disques de mon ordinateur. Elle permet de chercher des fichiers système que ne connait pas spotlight. Par rapport à la commande find, elle est beaucoup plus rapide car elle crée une base de données avec l'ensemble des fichiers et le chemin associée.

Seule contrainte : avoir une base de données à jour. Et là, grosse surprise, ma base n'est pas à jour, la commande locate ne sert à rien. La misère !

Reprenons par le commencement. Pour activer la commande locate qui ne l'est pas par défaut, il faut lancer cette commande dans le terminal :

    $ sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.locate.plist

Pour savoir comment fonctionne la programmation de travaux avec launchd, je vous renvoie [à un précédent article.]({filename}/demarrage-automatique-de-travaux-avec-launchd.markdown "démarrage automatique de travaux avec launchd")

Que contient le fichier plist ? Pour le savoir :

    $ sudo cat /System/Library/LaunchDaemons/com.apple.locate.plist

Ce qui donne :

    <plist version="1.0">
    <dict>
    	<key>Label</key>
    	<string>com.apple.locate</string>
    	<key>Disabled</key>
    	<true/>
    	<key>ProgramArguments</key>
    	<array>
    		<string>/usr/libexec/locate.updatedb</string>
    	</array>
    	<key>LowPriorityIO</key>
    	<true/>
    	<key>Nice</key>
    	<integer>5</integer>
    	<key>KeepAlive</key>
    	<dict>
    		<key>PathState</key>
    		<dict>
    			<key>/var/db/locate.database</key>
    			<false/>
    		</dict>
    	</dict>
    	<key>StartCalendarInterval</key>
    	<dict>
    		<key>Hour</key>
    		<integer>3</integer>
    		<key>Minute</key>
    		<integer>15</integer>
    		<key>Weekday</key>
    		<integer>6</integer>
    	</dict>
    	<key>AbandonProcessGroup</key>
    	<true/>
    </dict>
    </plist>

Et là, oh surprise, la commande de mise à jour de la base à savoir `/usr/libexec/locate.updatedb` ne se déclenche que le samedi à 3h15. Aucune chance d'avoir une base de données à jour.

Heureusement, il est toujours possible de lancer la mise à jour à la main avec

    $ sudo /usr/libexec/locate.updatedb

C'est un peu long, mais au moins, je suis sûr du résultat du locate.
