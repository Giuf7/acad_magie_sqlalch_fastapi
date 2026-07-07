import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from dal.models.base import Base


class RoleUser(str, enum.Enum):
    ELEVE = "Élève"
    PROFESSEUR = "Professeur"
    ADMIN = "Admin"


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(nullable=False)
    mot_de_passe: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[RoleUser] = mapped_column(nullable=False)

    # Lien optionnel vers un Élève OU un Professeur selon le rôle.

    eleve_id: Mapped[int | None] = mapped_column(ForeignKey("eleves.id"), nullable=True)
    professeur_id: Mapped[int | None] = mapped_column(
        ForeignKey("professeurs.id"), nullable=True
    )
