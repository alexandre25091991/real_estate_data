Projet en lien avec l'immobilier :
Mini Dashboard de suivi des prix immobiliers
Idée : Mettre en place une petite application Flask qui permet de suivre l’évolution des prix immobiliers dans une région ou une ville donnée.

Fonctionnalités proposées :
Recherche de prix immobiliers : Intégration d'une API (comme l'API de MeilleursAgents ou Zillow pour les États-Unis) pour récupérer les prix immobiliers actuels dans une ville ou un quartier donné.

Historique des prix : Enregistrer les données de prix récupérées via l'API dans une base de données (SQLite pour la simplicité) et permettre à l’utilisateur de consulter l’évolution des prix dans une interface simple en HTML.

Graphique d’évolution des prix : Utiliser une bibliothèque Python comme Matplotlib pour générer un graphique montrant l’évolution des prix dans la zone choisie, qui sera affiché sur la page HTML.

Backend (Flask):
Appel à l’API pour récupérer les prix.
Enregistrement et lecture dans la base de données (SQLite).
Génération de graphiques avec Matplotlib.
Frontend (HTML):
Formulaire simple pour entrer la ville ou le quartier.
Affichage des données sous forme de tableau et graphique.

Installation pour faire fonctionner l'application: 

pip install Flask
