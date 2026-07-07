import enum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dal.models.base import Base

if TYPE_CHECKING:
    from dal.models.maison import Maison


class StatutEleve(str, enum.Enum):
    ACTIF = "Actif"
    DIPLOME = "Diplômé"
    RENVOYE = "Renvoyé"


class Eleve(Base):
    __tablename__ = "eleves"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(nullable=False)
    annee: Mapped[int] = mapped_column(nullable=False)
    familier: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[StatutEleve] = mapped_column(nullable=False)

    # Plusieurs élèves peuvent avoir une seule maison
    # Many to One
    maison_id: Mapped[int] = mapped_column(ForeignKey("maisons.id"))
    maison: Mapped["Maison"] = relationship("Maison", back_populates="eleves")
