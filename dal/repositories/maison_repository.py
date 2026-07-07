from sqlalchemy.orm import Session

from dal.models.maison import Maison

class MaisonRepository:

    def get_all(self, db: Session) -> list[Maison]:
        return db.query(Session).all()
    
    def get_by_id(self, db: Session, maison_id: int) -> Maison | None:
        return db.query(Maison).filter(Maison.id == maison_id).first()
    
    def create(self, db: Session, data: dict) -> Maison:
        maison = Maison(**data)
        db.add(maison)
        db.flush()
        db.refresh(maison)
        return maison
    
    def update(self, db: Session, maison: Maison, data: dict) -> Maison:
        for field, value in data.items():
            setattr(maison, field, value)
        db.flush()
        db.refresh(maison)
        return maison
    
    def delete(self, db: Session, maison: Maison) -> None:
        db.delete(maison)
        db.flush