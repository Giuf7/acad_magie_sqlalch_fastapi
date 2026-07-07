from pydantic import BaseModel, ConfigDict

class ProfesseurBase(BaseModel):
    nom_prof: str
    anciennete: int

class ProfesseurCreate(ProfesseurBase):
    pass

class ProfesseurUpdate(BaseModel):
    nom_prof: str
    anciennete: int

class ProfesseurResponse(ProfesseurBase):
    id: int

    model_config = ConfigDict(from_attributes=True)