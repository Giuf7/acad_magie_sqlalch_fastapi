import enum

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
    lien: Mapped[str] = mapped_column(nullable=True)
