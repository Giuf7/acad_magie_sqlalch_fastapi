from sqlalchemy.orm import Session

from dal.models.professeur import Professeur

class ProfesseurRepository:

    def get_all(self, db: Session) -> list[Professeur]:
        return db.query(Session).all()
    
    def get_by_id(self, db: Session, professeur_id: int) -> Professeur | None:
        return db.query(Professeur).filter(Professeur.id == professeur_id).first()
    
    def create(self, db: Session, data: dict) -> Professeur:
        professeur = Professeur(**data)
        db.add(professeur)
        db.flush()
        db.refresh(professeur)
        return professeur
    
    def update(self, db: Session, professeur: Professeur, data: dict) -> Professeur:
        for field, value in data.items():
            setattr(professeur, field, value)
        db.flush()
        db.refresh(professeur)
        return professeur
    
    def delete(self, db: Session, professeur: Professeur) -> None:
        db.delete(professeur)
        db.flush
    
    