from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from dal.repositories.eleve_repository import EleveRepository
from api.schemas.schema_eleve import EleveCreate, EleveUpdate

repository = EleveRepository()

def list_eleve(db: Session):
    return repository.get_all(db)

def get_eleve(db: Session, eleve_id: int):
    eleve = repository.get_by_id(db, eleve_id)
    if eleve is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Eleves {eleve_id} introuvable",
        )
    return eleve

def create_eleve(db: Session, data: EleveCreate):
    return repository.create(db, data.model_dump())

def update_eleve(db: Session, eleve_id: int, data: EleveUpdate):
    eleve = get_eleve(db, eleve_id)
    return repository.update(db, eleve, data.model_dump(exclude_unset=True))

def delete_eleve(db: Session, eleve_id: int) -> None:
    eleve = get_eleve(db, eleve_id)
    repository.delete(db, eleve)