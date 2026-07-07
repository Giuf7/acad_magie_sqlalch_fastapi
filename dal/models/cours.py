from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dal.models.base import Base

if TYPE_CHECKING:
    from dal.models.professeur import Professeur


class Cours(Base):
    __tablename__ = "cours"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(nullable=False)
    annee: Mapped[int] = mapped_column(nullable=False)
    capacite: Mapped[int] = mapped_column(nullable=False)
    responsable: Mapped[str] = mapped_column(nullable=False)

    # Many to One
    professeur_id: Mapped[int] = mapped_column(ForeignKey("professeurs.id"))
    professeur: Mapped["Professeur"] = relationship(
        "Professeur", back_populates="cours"
    )
