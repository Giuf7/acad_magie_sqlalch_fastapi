from pydantic import BaseModel, ConfigDict

# DTO de base avec les champs communs
class CoursBase(BaseModel):
    nom: str
    annee: int
    capacite: int
    responsable: str
    professeur_id: int

# DTO pour la création (données requises en entrée)
class CoursCreate(CoursBase):
    pass

# DTO pour la mise à jour (tous les champs deviennent optionnels)
class CoursUpdate(BaseModel):
    nom: str | None = None
    annee: int | None = None
    capacite: int | None = None
    responsable: str | None = None
    professeur_id: int | None = None

# DTO pour la réponse (ce que l'API renvoie)
class CoursResponse(CoursBase):
    id: int

    # Permet à Pydantic de lire les objets SQLAlchemy directement
    model_config = ConfigDict(from_attributes=True)