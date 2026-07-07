from pydantic import BaseModel, ConfigDict

class MaisonBase(BaseModel):
    nom: str
    couleur: str
    fondateur: str
    valeurs: str

class MaisonCreate(MaisonBase):
    pass

class MaisonUpdate(BaseModel):
    nom: str | None = None
    couleur: str | None = None
    fondateur: str | None = None
    valeurs: str | None = None

class MaisonResponse(MaisonBase):
    id: int

    model_config = ConfigDict(from_attributes=True)