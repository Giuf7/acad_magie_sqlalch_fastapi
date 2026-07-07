from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dal.database import get_db_session
from api.controllers import controllers_eleve
from api.schemas.schema_eleve import EleveCreate, EleveUpdate, EleveResponse

router = APIRouter(prefix="/eleve", tags=["Eleves"])

@router.get("/", response_model=list[EleveResponse])
def list_eleve(db: Session = Depends(get_db_session)):
    return controllers_eleve.list_eleve(db)

@router.get("/{eleve_id}", response_model=EleveResponse)
def get_eleve(eleve_id: int, db: Session = Depends(get_db_session)):
    return controllers_eleve.get_eleve(db, eleve_id)

@router.post("/", response_model=EleveResponse, status_code=status.HTTP_201_CREATED)
def create_eleve(data: EleveCreate, db: Session = Depends(get_db_session)):
    return controllers_eleve.create_eleve(db, data)

@router.put("/{eleve_id}", response_model=EleveResponse)
def update_eleve(
    eleve_id: int, data: EleveUpdate, db: Session = Depends(get_db_session)
):
    return controllers_eleve.update_eleve(db, eleve_id, data)

@router.delete("/{eleve_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_eleve(eleve_id: int, db: Session = Depends(get_db_session)):
    controllers_eleve.delete_eleve(db, eleve_id)