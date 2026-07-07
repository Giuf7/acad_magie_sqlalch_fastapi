from sqlalchemy.orm import Session

from dal.models.cours import Cours


class CoursRepository:

    def get_all(self, db: Session) -> list[Cours]:
        return db.query(Cours).all()

    def get_by_id(self, db: Session, cours_id: int) -> Cours | None:
        return db.query(Cours).filter(Cours.id == cours_id).first()

    def create(self, db: Session, data: dict) -> Cours:
        cours = Cours(**data)
        db.add(cours)
        db.flush()
        db.refresh(cours)
        return cours

    def update(self, db: Session, cours: Cours, data: dict) -> Cours:
        for field, value in data.items():
            setattr(cours, field, value)
        db.flush()
        db.refresh(cours)
        return cours

    def delete(self, db: Session, cours: Cours) -> None:
        db.delete(cours)
        db.flush()
