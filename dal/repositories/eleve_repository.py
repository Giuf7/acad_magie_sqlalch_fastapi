from sqlalchemy.orm import Session

from dal.models.eleve import Eleve

class EleveRepository:

    def get_all(self, db: Session) -> list[Eleve]:
        return db.query(Eleve).all()

    def get_by_id(self, db: Session, eleves_id: int) -> Eleve | None:
        return db.query(Eleve).filter(Eleve.id == eleves_id).first()

    def create(self, db: Session, data: dict) -> Eleve:
        eleves = Eleve(**data)
        db.add(eleves)
        db.flush()
        db.refresh(eleves)
        return eleves

    def update(self, db: Session, eleves: Eleve, data: dict) -> Eleve:
        for field, value in data.items():
            setattr(eleves, field, value)
        db.flush()
        db.refresh(eleves)
        return eleves

    def delete(self, db: Session, eleves: Eleve) -> None:
        db.delete(eleves)
        db.flush()