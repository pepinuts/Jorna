# Training App (FastAPI + React) — Starter

Un squelette minimal pour démarrer **brique par brique** :
- API FastAPI avec `GET /health`
- Front React (Vite + TS) qui appelle `/health`
- Postgres prêt (même si pas encore utilisé)
- Docker Compose pour lancer tout en 1 commande

## Prérequis
- Docker + Docker Compose

## Lancer en dev
```bash
docker compose up --build
```

- Front: http://localhost:5173
- API: http://localhost:8000/docs (Swagger)

## Structure
- `backend/` : FastAPI
- `frontend/` : React (Vite)
- `docker-compose.yml` : orchestration

## Prochaine brique suggérée
1) Ajouter SQLAlchemy + Alembic (migrations)
2) Créer les 3 tables MVP: `users`, `activities`, `plan_items`
3) CRUD simple: `plan_items` (séances planifiées)
