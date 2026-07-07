from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from dal.models.base import Base

if TYPE_CHECKING:
    from dal.models.eleve import Eleve


class Maison(Base):
    __tablename__ = "maisons"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(nullable=False)
    couleur: Mapped[str] = mapped_column(nullable=False)
    fondateur: Mapped[str] = mapped_column(nullable=False)
    valeurs: Mapped[str] = mapped_column(nullable=False)

    # Une maison peut accueillir plusieurs élèves.
    # Relation one to many
    eleves: Mapped[List["Eleve"]] = relationship(
        "Eleve", back_populates="maison", cascade="all, delete-orphan"
    )
