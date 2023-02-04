#!/bin/sh
# cliquer pour démarrer, cliquer pour arrêter

TEST=$(ps -ef | grep conky | grep meteo)

if [ "$TEST" != "" ]; then 
    exec ps -ef | grep conky | grep meteo | awk '{print $2}'| xargs kill
else
    conky -c ~/.conky/.conkyrc_meteo
    conky -c ~/.conky/.conkyrc_meteo_jour2
    conky -c ~/.conky/.conkyrc_meteo_jour3
    conky -c ~/.conky/.conkyrc_meteo_jour4
exit
fi
