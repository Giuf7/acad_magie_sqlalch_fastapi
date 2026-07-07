from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dal.database import get_db_session
from api.controllers import controllers_professeur
from api.schemas.schema_professeur import ProfesseurCreate, ProfesseurResponse, ProfesseurUpdate

router = APIRouter(prefix="/professeur", tags=["Professeurs"])

@router.get("/", response_model=list[ProfesseurResponse])
def list_professeur(db : Session = Depends(get_db_session)):
    return controllers_professeur.list_professeur(db)

@router.get("/{professeur_id}", response_model=ProfesseurResponse)
def get_professeur(professeur_id: int, db : Session = Depends(get_db_session)):
    return controllers_professeur.get_professeur(db, professeur_id)

@router.post("/", response_model=ProfesseurResponse, status_code=status.HTTP_201_CREATED)
def create_professeur(data: ProfesseurCreate, db : Session = Depends(get_db_session)):
    return controllers_professeur.create_professeur(db, data)

@router.put("/{professeur_id}", response_model=ProfesseurResponse)
def update_professeur(
    professeur_id: int, data: ProfesseurUpdate, db: Session = Depends(get_db_session)
):
    return controllers_professeur.update_professeur(db, professeur_id, data)

@router.delete("/{professeur_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_professeur(professeur_id: int, db : Session = Depends(get_db_session)):
    controllers_professeur.delete_professeur(db, professeur_id)