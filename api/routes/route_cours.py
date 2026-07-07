from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dal.database import get_db_session
from api.controllers import controllers_cours
from api.schemas.schema_cours import CoursCreate, CoursUpdate, CoursResponse

router = APIRouter(prefix="/cours", tags=["Cours"])

@router.get("/", response_model=list[CoursResponse])
def list_cours(db: Session = Depends(get_db_session)):
    return controllers_cours.list_cours(db)

@router.get("/{cours_id}", response_model=CoursResponse)
def get_cours(cours_id: int, db: Session = Depends(get_db_session)):
    return controllers_cours.get_cours(db, cours_id)

@router.post("/", response_model=CoursResponse, status_code=status.HTTP_201_CREATED)
def create_cours(data: CoursCreate, db: Session = Depends(get_db_session)):
    return controllers_cours.create_cours(db, data)

@router.put("/{cours_id}", response_model=CoursResponse)
def update_cours(
    cours_id: int, data: CoursUpdate, db: Session = Depends(get_db_session)
):
    return controllers_cours.update_cours(db, cours_id, data)

@router.delete("/{cours_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cours(cours_id: int, db: Session = Depends(get_db_session)):
    controllers_cours.delete_cours(db, cours_id)