# 🪄 L'Académie de Sorcellerie — API

API REST de gestion de la vie académique de l'Académie (maisons, professeurs, cours, élèves).
Construite avec **FastAPI** + **SQLAlchemy** (SQLite).

> ⚠️ Projet pédagogique. Les mots de passe sont stockés **en clair** — c'est temporaire et assumé pour l'exercice.

## Prérequis

- Python **3.12+**

## Installation

```bash
# 1. Créer et activer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate

# 2. Installer les dépendances
pip install -r requirements.txt
```

## Lancer l'API

```bash
python -m uvicorn api.app:app --reload --port 5000
```

L'API est alors disponible sur **http://127.0.0.1:5000**.

Au premier démarrage, la base SQLite `magic.db` est créée automatiquement et les tables sont initialisées.

## Documentation interactive

FastAPI génère une doc Swagger auto :

- **Swagger UI** : http://127.0.0.1:5000/docs
- **ReDoc** : http://127.0.0.1:5000/redoc

Tu peux y tester tous les endpoints directement depuis le navigateur.

## Endpoints disponibles

| Ressource | Préfixe | Opérations |
|-----------|---------|------------|
| Maisons | `/maison` | CRUD complet |
| Professeurs | `/professeur` | CRUD complet |
| Cours | `/cours` | CRUD complet |
| Élèves | `/eleve` | CRUD complet |

## Réinitialiser la base

Pour repartir d'une base vierge (par ex. après un changement de modèle) :

```bash
rm magic.db
```

Elle sera recréée au prochain lancement.

## Structure du projet

```
api/                 # Couche web (FastAPI)
  app.py             # Point d'entrée + montage des routes
  routes/            # Définition des endpoints
  controllers/       # Logique applicative
  schemas/           # Schémas Pydantic (validation entrée/sortie)
dal/                 # Data Access Layer
  database.py        # Connexion + init de la base
  models/            # Modèles SQLAlchemy
  repositories/      # Accès aux données (CRUD)
```
