from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dal.database import get_db_session
from dal.models.utilisateur import Utilisateur
from api.controllers import controllers_utilisateur
from api.auth import get_current_user
from api.schemas.schema_utilisateur import LoginRequest, LoginResponse

router = APIRouter(tags=["Utilisateurs"])

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db_session)):
    return controllers_utilisateur.login(db, data)

@router.get("/me", response_model=LoginResponse)
def me(current_user: Utilisateur = Depends(get_current_user)):
    """Renvoie l'utilisateur courant, identifié via l'en-tête X-User-Id."""
    return current_user
