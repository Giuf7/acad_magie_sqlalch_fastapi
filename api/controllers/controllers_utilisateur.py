from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from dal.repositories.utilisateur_repository import UtilisateurRepository
from api.schemas.schema_utilisateur import LoginRequest

repository = UtilisateurRepository()


def login(db: Session, data: LoginRequest):
    utilisateur = repository.get_by_email(db, data.email)

    if utilisateur is None or utilisateur.mot_de_passe != data.mot_de_passe:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants invalides",
        )
    return utilisateur
