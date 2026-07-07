from pydantic import BaseModel, ConfigDict

class EleveBase(BaseModel):
    nom: str
    annee: int
    familier: str
    status: str
    maison_id: int

class EleveCreate(EleveBase):
    pass

class EleveUpdate(BaseModel):
    nom: str | None = None
    annee: int | None = None
    familier: str | None = None
    status: str | None = None
    maison_id: int | None = None

class EleveResponse(EleveBase):
    id: int

    model_config = ConfigDict(from_attributes=True)