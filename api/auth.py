"""Dépendances d'autorisation partagées par les routes.

Authentification SIMULÉE (sécurité hors scope pour l'exercice) : le client
annonce son identité via l'en-tête HTTP `X-User-Id`. Le serveur le croit, mais
recharge l'utilisateur réel en base pour lire son rôle. N'importe qui pourrait
usurper un id aujourd'hui — ce sera remplacé par une vraie auth (token signé)
plus tard.
"""

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from dal.database import get_db_session
from dal.models.utilisateur import Utilisateur, RoleUser
from dal.repositories.utilisateur_repository import UtilisateurRepository

repository = UtilisateurRepository()


def get_current_user(
    x_user_id: int | None = Header(default=None),
    db: Session = Depends(get_db_session),
) -> Utilisateur:
    """Identifie l'appelant à partir de l'en-tête `X-User-Id`.

    Header optionnel + exception manuelle : on garde ainsi la main sur le code
    d'erreur (401 explicite) au lieu du 422 automatique de FastAPI.
    """
    if x_user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="En-tête X-User-Id requis",
        )

    utilisateur = repository.get_by_id(db, x_user_id)
    if utilisateur is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilisateur inconnu",
        )

    return utilisateur


def require_admin(
    current_user: Utilisateur = Depends(get_current_user),
) -> Utilisateur:
    """Restreint un endpoint aux administrateurs.

    403 = authentifié mais pas les droits (à distinguer du 401 = pas d'identité).
    """
    if current_user.role != RoleUser.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Réservé aux administrateurs",
        )
    return current_user
