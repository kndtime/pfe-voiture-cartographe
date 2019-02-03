# PFE VOITURE CARTOGRAPHE -- Viewer
=======================

## Introduction
Ce projet fut développé pour notre PFE à l'EPITA.
Son but est d'automatiser la mesure des pentes et des dévers des trottoirs.
Cette partie regroupe le code pour la visualization des données.

## Pré-requis

Pour le developpement, vous aurez uniquement besoin d'avoir Node.js d'installé. Et pensez à utiliser une config editor approprié [Editorconfig](http://editorconfig.org/)
(pas obligatoire).

### Node

[Node](http://nodejs.org/) est vraiment facile à installer et inclus maintenant [NPM](https://npmjs.org/).
VOus devriez être capable d'utiliser les commandes suivantes lors après installation.

    $ node --version
    v0.10.24

    $ npm --version
    1.3.21

#### Installation de Node sur OS X

Vous aurez besoin d'utiliser Terminal. Sur OSX, vous pouvez l'ouvrir avec ce chemin par défaut.

`/Applications/Utilities/Terminal.app`.

Intallez [Homebrew](http://brew.sh/), si ce n'est pas déjà fait avec la commande suivante.

    $ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

Si tout a bien fonctionnée, vous pouvez lancer

    brew install node

#### Installation de Node sur Linux

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install nodejs

#### Installation de Node sur Windows

Allez sur le [site officiel de Node.js](http://nodejs.org/) et télécharger l'installeur.
Evidemment, ayez sur d'avoir git de disponible dans votre path car 'npm' en aura sans doûte besoin.

---

## Installation des sources

    $ git clone https://gitlab.com/kinl27/pfe-voiture-cartographe.git
    $ cd pfe-voiture-cartographe/viewver
    $ npm install

## Start & watch

    $ npm start

## Compiler vers prod

    $ npm run build

## Mise à jour des dépendences

Certains paquets sont souvent mis à jours, n'hésitez donc pas à utiliser `npm prune` & `npm install`.

    $ git pull
    $ npm prune
    $ npm install

Vous pouvez combiner ces trois commandes en faisant :

    $ npm run pull

## Languages & tools

### JavaScript

- [React](http://facebook.github.io/react) is used for UI.

### Template

- [Material Dashboard React ](https://github.com/creativetimofficial/material-dashboard-react) utilisé comme base pour réaliser des vues un minimun jolies.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
