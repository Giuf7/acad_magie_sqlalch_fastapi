from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dal.database import get_db_session
from api.controllers import controllers_maison
from api.schemas.schema_maison import MaisonCreate, MaisonUpdate, MaisonResponse

router = APIRouter(prefix="/maison", tags=["Maisons"])

@router.get("/", response_model=list[MaisonResponse])
def list_maison(db : Session = Depends(get_db_session)):
    return controllers_maison.list_maison(db)

@router.get("/{maison_id}", response_model=MaisonResponse)
def get_maison(maison_id: int, db : Session = Depends(get_db_session)):
    return controllers_maison.get_maison(db, maison_id)

@router.post("/", response_model=MaisonResponse, status_code=status.HTTP_201_CREATED)
def create_maison(data: MaisonCreate, db : Session = Depends(get_db_session)):
    return controllers_maison.create_maison(db, data)

@router.put("/{maison_id}", response_model=MaisonResponse)
def update_maison(
    maison_id: int, data: MaisonUpdate, db: Session = Depends(get_db_session)
):
    return controllers_maison.update_maison(db, maison_id, data)

@router.delete("/{maison_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maison(maison_id: int, db : Session = Depends(get_db_session)):
    controllers_maison.delete_maison(db, maison_id)