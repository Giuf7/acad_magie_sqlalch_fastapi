from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from dal.repositories.maison_repository import MaisonRepository
from api.schemas.schema_maison import MaisonCreate, MaisonUpdate

repository = MaisonRepository()

def list_maison(db: Session):
    return repository.get_all(db)

def get_maison(db: Session, maison_id: int):
    maison = repository.get_by_id(db, maison_id)
    if maison is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Maison {maison_id} introuvable",
        )
    return maison

def create_maison(db: Session, data: MaisonCreate):
    return repository.create(db, data.model_dump())

def update_maison(db: Session, maison_id: int, data: MaisonUpdate):
    maison = get_maison(db, maison_id)
    return repository.update(db, maison, data.model_dump(exclude_unset=True))

def delete_maison(db : Session, maison_id: int) -> None :
    maison = get_maison(db, maison_id)
    repository.delete(db, maison)