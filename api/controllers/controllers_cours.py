from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from dal.repositories.cours_repository import CoursRepository
from api.schemas.schema_cours import CoursCreate, CoursUpdate

repository = CoursRepository()


def list_cours(db: Session):
    return repository.get_all(db)


def get_cours(db: Session, cours_id: int):
    cours = repository.get_by_id(db, cours_id)
    if cours is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cours {cours_id} introuvable",
        )
    return cours


def create_cours(db: Session, data: CoursCreate):
    return repository.create(db, data.model_dump())


def update_cours(db: Session, cours_id: int, data: CoursUpdate):
    cours = get_cours(db, cours_id)
    return repository.update(db, cours, data.model_dump(exclude_unset=True))


def delete_cours(db: Session, cours_id: int) -> None:
    cours = get_cours(db, cours_id)
    repository.delete(db, cours)
