from pydantic import BaseModel, ConfigDict

class LoginRequest(BaseModel):
    email: str
    mot_de_passe: str

class LoginResponse(BaseModel):
    id: int
    email: str
    role: str
    eleve_id: int | None = None
    professeur_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
