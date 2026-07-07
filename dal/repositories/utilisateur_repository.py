from sqlalchemy.orm import Session

from dal.models.utilisateur import Utilisateur

class UtilisateurRepository:

    def get_all(self, db: Session) -> list[Utilisateur]:
        return db.query(Session).all()
    
    def get_by_id(self, db: Session, utilisateur_id: int) -> Utilisateur | None:
        return db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    
    def create(self, db: Session, data: dict) -> Utilisateur:
        utilisateur = Utilisateur(**data)
        db.add(utilisateur)
        db.flush()
        db.refresh(utilisateur)
        return utilisateur
    
    def update(self, db: Session, utilisateur: Utilisateur, data: dict) -> Utilisateur:
        for field, value in data.items():
            setattr(utilisateur, field, value)
        db.flush()
        db.refresh(utilisateur)
        return utilisateur
    
    def delete(self, db: Session, utilisateur: Utilisateur) -> None:
        db.delete(utilisateur)
        db.flush
    
    