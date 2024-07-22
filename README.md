# Étude de cas technique back-end

>⏱️ Temps imparti : 1 jour (à compter de la date d’envoi du sujet)

## Description

Dans ce petit cas pratique, nous évaluerons vos connaissances techniques en back-end, et plus particulièrement le framework Django sous l’architecture REST.

L’objectif est de : 

- Compléter le code pour rendre l’application fonctionnelle (sans toucher aux Models)
- Transformer un mini projet Django existant en une API Django REST

Plus concrètement, il s’agit d’une mini-application appelée “Prestations” qui s’articule autour d’un Model (Prestation). 

Vous serez amené à travailler sur toute les opérations CRUD autour de cet objet, avant de transformer cette application en API REST (Django REST Framework).

Vous trouverez un résumé de toutes les TODO dans le code source de l'application, mais également en bas de cette page.

---

## Déroulement

Pour commencer cette mission, vous devez :
      ⬇️ Cloner le repo suivant : https://bit.ly/repo-exercice-django

🌲 Créer une branche distincte appelée `feat/todo-exercice-django`

👨‍💻 Ouvrir votre IDE préféré

🏃🏻‍♂️ Appliquer les migrations 
→ exécuter `python manage.py makemigrations` puis `python manage.py migrate`

🔎 Prendre connaissance du projet et commencer à coder !


> ⚠️ **Remarque :** Vous trouverez également des TODO Bonus. Elles ne sont pas obligatoires pour terminer cette mission mais seront des gros plus. N'hésitez pas à mettre en valeur vos compétences en programmation 💪

> ⚠️ **Important :** Les bonnes pratiques de développement seront également évaluées (recours à des variables d’environnements, commentaires, …)

> ⚠️ **Important :** Cet exercice teste vos propres aptitudes personnelles. Il va donc de soi que tout recours à une aide extérieure pour le faire à votre place est prohibé et disqualifiant. Néanmoins, vous pouvez bien sûr vous aider ponctuellement de ressources pour vous débloquer (comme un vrai dev 😉 )

---

## Liste des TODO

Pour faciliter les choses, voici une liste de tous les TODO :

### Application

- [ ]  Créer les vues pour les opérations CRUD
- [ ]  Créer les formulaires pour les modèles
- [ ]  Créer les templates HTML pour les vues (le style n’est pas évalué, vous pouvez utiliser le front de votre choix)
- [ ]  Configurer les URLs de l'application
- [ ]  (Bonus) Configurer l'administration Django

### REST API

- [ ]  Configurer Django REST Framework
- [ ]  Créer les serializers pour les modèles.
- [ ]  Créer les vues API pour les opérations CRUD (basées sur des APIViews ou ViewSets)
- [ ]  Configurer les routes API
- [ ]  Tester les endpoints API

### Tests

- [ ]  Créer une base de données locale (SQLite) de Clients, Suppliers, et Prestations
- [ ]  Écrire des tests unitaires pour les vues Django et les vues API.
- [ ]  (Bonus) Écrire des tests d'intégration pour s'assurer que les différents composants de l'application fonctionnent bien ensemble.

### Documentation (bonus)

- [ ]  Générer automatiquement la documentation de l'API en utilisant Swagger ou OpenAPI grâce à des librairies comme `drf-yasg` ou `drf-spectacular`
- [ ]  Ajouter des descriptions et des exemples d'utilisation pour chaque endpoint dans la documentation de l'API.

### Authentification (bonus)

- [ ]  Implémenter une authentification simple basée sur des tokens avec Django REST Framework (DRF).
- [ ]  Mettre en place l'authentification JWT (JSON Web Tokens) en utilisant `djangorestframework-simplejwt` ou un autre package similaire.
- [ ]  Ajouter des permissions personnalisées pour restreindre l'accès à certaines vues API (par exemple, seules les prestations créées par l'utilisateur actuel peuvent être modifiées par lui).

## Soumission de la mission

Vous pouvez soumettre votre mission en créant une demande de fusion (merge request) sur Github pour votre branche `feat/todo-exercice-django`.

C'est tout, bonne chance ! 🚀

> 💡 Si vous avez des questions concernant l'exercice ou pendant sa réalisation, veuillez me contacter par email à [cto@deplano.fr](mailto:cto@deplano.fr)
