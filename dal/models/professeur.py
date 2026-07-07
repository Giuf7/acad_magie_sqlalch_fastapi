from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from dal.models.base import Base

if TYPE_CHECKING:
    from dal.models.cours import Cours


class Professeur(Base):
    __tablename__ = "professeurs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_prof: Mapped[str] = mapped_column(nullable=False)
    anciennete: Mapped[int] = mapped_column(nullable=False)

    # One to Many
    cours: Mapped[List["Cours"]] = relationship(
        "Cours", back_populates="professeur", cascade="all, delete-orphan"
    )