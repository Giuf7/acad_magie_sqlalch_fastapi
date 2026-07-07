from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from dal.repositories.professeur_repository import ProfesseurRepository
from api.schemas.schema_professeur import ProfesseurCreate, ProfesseurUpdate

repository = ProfesseurRepository()

def list_professeur(db: Session):
    return repository.get_all(db)

def get_professeur(db: Session, professeur_id: int):
    professeur = repository.get_by_id(db, professeur_id)
    if professeur is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Professeur {professeur_id} introuvable",
        )
    return professeur

def create_professeur(db: Session, data: ProfesseurCreate):
    return repository.create(db, data.model_dump())

def update_professeur(db: Session, professeur_id: int, data: ProfesseurUpdate ):
    professeur = get_professeur(db, professeur_id)
    return repository.update(db, professeur, data.model_dump(exclude_unset=True))

def delete_professeur(db: Session, professeur_id : int) -> None :
    professeur = get_professeur(db, professeur_id)
    repository.delete(db, professeur)