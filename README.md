PFE VOITURE CARTOGRAPHE
=======================

## Introduction
Ce projet fut développé pour notre PFE à l'EPITA.
Son but est d'automatiser la mesure des pentes et des dévers des trottoirs.

## Installation

Ce projet utililse le framework ROS pour mesurer la pente et les dévers des trottoirs.

Pour pouvoir utiliser ce projet, il faut:
* une raspberry pi (avec raspbian ou Ubuntu Mate);
* y brancher un gyroscope MPU6050 en I2C et un GPS Ublox c94-m8p en USB;
* y installer ROS kinetic;
* cloner ce projet dans le répertoire de travail ROS;
* cloner le driver ROS NMEA disponible [ici](https://github.com/ros-drivers/nmea_navsat_driver) dans le répertoire de travail ROS;
* installer la carte et les capteurs sur un vecteur mobile (potentiellement motorisé), de façon à ce que le gyroscope soit droit.

## Utilisation
Pour pouvoir lancer ce projet, il faut d'abord le compiler après l'avoir cloné:
```
$ cd ~/<repertoire_de_travail_catkin>/
$ catkin_make
```
puis lancer les commandes suivantes:
```
$ source devel/setup.bash
$ roslaunch buggy_sensor buggySensorLaunch.launch
```

ROS affichera alors des logs de manière régulière à l'écran:
* 'STOP' -> il faut mettre le vecteur motorisé à l'arrêt, jusqu'à ce qu'il affiche le log de ses mesures;
* le log de ses mesures, une fois affiché l'on peut déplacer le vecteur motorisé;

## Structure

Le package **buggy\_sensor** contient 4 noeuds ROS nécéssaires à la mesure des angles et des coordonnées GPS:
* MPU6050\_talker.py mesure les angles à l'aide du gyroscope MPU6050, en utilisant des formules mathématiques expliquées dans [cet article](http://www.hobbytronics.co.uk/accelerometer-info).Il envoie les données mesurées sur le topic 'MPU6050Talker'.
* buggy\_mainListener.py récupère les données mesurées par le gyroscope et l'accéléromètre, et attends l'interruption envoyée par le noeud buggy\_waitInterrupt.py pour enregistrer ces mesures dans un fichier csv et les envoyer sur l'interface web.	* buggy\_waitInterrupt.py envoie un message sur le topic 'buggyInterrupt' de manière régulière selon un intervalle de temps donné, afin de signifier au noeud buggy\_mainListener d'enregistrer ses mesures. La période entre chaque mesure peut être modifiée dans ce noeud si besoin.
* buggy\_server.py envoie des informations sur la carte (RAM, CPU, disque) à l'interface web.

le dossier **capteur** contient:
* le premier script , **mesure.py** (développé sans ROS) mesurant les angles et les écrivant dans un fichier CSV.
* le script d'importation sur OpenStreetMap, importData.py, qui prend en paramètre un fichier CSV contenant des mesures, et un fichier contenant un commentaire pour importer ces données. Pour plus d'informations, vous pouvez entrer la commande ``` $ ./importData.py --help```.

## Visualisation des données
 Afin de pouvoir se connecter avec le noeud ROS, l'interface Web à besoin d'établir une connection avec [ROS\_bridge](https://github.com/RobotWebTools/rosbridge_suite) qui est un module ROS.

### Utilisation
```
$ cd ~/<repertoire_de_travail_catkin>/
$ source devel/setup.bash
$ roscore &
$ roslaunch rosbridge_server rosbridge_websocket.launch
$ roslaunch buggy_sensor buggySensorLaunch.launch
$ cd ~/../pfe_voiture_cartographe/viewer
$ npm start
```
Après cela vous deviez avoir un webserver qui tourne sur le port 8080 (par défaut) et une interface web qui écoute sur ce port.
Consultez le [README.md](https://gitlab.com/kinl27/pfe-voiture-cartographe/blob/master/viewer/README.md) dans Viever pour plus de détails.
