from contextlib import asynccontextmanager

from fastapi import FastAPI

from dal.database import init_db, test_connexion
from api.routes import route_cours, route_eleve, route_maison, route_professeur


@asynccontextmanager
async def lifespan(app: FastAPI):
    if test_connexion():
        init_db(delete=False)
        print("[OK] Db initialisee avec succes")
    yield


app = FastAPI(
    title="API Academie de Magie",
    description="Gestion des cours, professeurs, eleves et maisons.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(route_cours.router)
app.include_router(route_eleve.router)
app.include_router(route_maison.router)
app.include_router(route_professeur.router)


@app.get("/", tags=["Racine"])
def racine():
    return {"message": "Bienvenue sur l'API de l'Academie de Magie"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api.app:app", host="0.0.0.0", port=5000, reload=True)
