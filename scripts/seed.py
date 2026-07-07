import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dal.database import get_db, init_db
from dal.models.cours import Cours
from dal.models.eleve import Eleve, StatutEleve
from dal.models.maison import Maison
from dal.models.professeur import Professeur
from dal.models.utilisateur import Utilisateur, RoleUser

MOT_DE_PASSE = "magie123"


def _slug(nom: str) -> str:
    """Prénom sans accents, en minuscules (pour construire les emails)."""
    sans_accents = (
        unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode()
    )
    return sans_accents.lower().split()[0]

MAISONS = [
    ("Pyrelame", "Écarlate", "Ignatia Braise", "Courage et audace"),
    ("Ondiris", "Azur", "Marée Sereine", "Sagesse et sérénité"),
    ("Sylvenroc", "Émeraude", "Sylvain Racine", "Loyauté et patience"),
    ("Ombrelin", "Argent", "Noctem Voile", "Ruse et ambition"),
]

PROFESSEURS = [
    ("Aldric Fulmen", 22),
    ("Morgane Sortilège", 15),
    ("Cassius Venin", 30),
    ("Ophélie Brume", 8),
    ("Ravian Métamorphe", 12),
    ("Selena Astralis", 19),
]

COURS = [
    ("Sortilèges élémentaires", 1, 30, 0),
    ("Potions fondamentales", 2, 20, 2),
    ("Défense contre les forces obscures", 3, 25, 0),
    ("Botanique magique", 2, 22, 3),
    ("Métamorphose avancée", 4, 18, 4),
    ("Divination et astres", 5, 15, 5),
    ("Duel et stratégie", 6, 16, 1),
]

NOMS_ELEVES = [
    "Elara Vent", "Tobias Ronce", "Lyra Solis", "Cedric Aube", "Nyla Brume",
    "Orin Faucon", "Mira Sable", "Gaspard Ombre", "Isolde Rive", "Basile Cendre",
    "Faye Lumen", "Rowan Épine", "Cassia Nox", "Dorian Givre", "Selene Aster",
    "Milo Bruyère", "Anouk Verne", "Thibault Roc", "Prune Saule", "Elias Mont",
    "Rhea Corail", "Silas Braise", "Ondine Flot", "Malo Volt", "Livia Plume",
    "Aksel Fjord", "Nora Sylve", "Timeo Souffle", "Vesna Aurore", "Léandre Val",
    "Iris Mésange", "Owen Silex",
]

FAMILIERS = [
    "Hibou", "Chat noir", "Crapaud", "Corbeau",
    "Rat", "Serpent", "Faucon", "Chauve-souris",
]


def seed() -> None:
    init_db(delete=True)

    with get_db() as db:
        maisons = [
            Maison(nom=nom, couleur=couleur, fondateur=fondateur, valeurs=valeurs)
            for nom, couleur, fondateur, valeurs in MAISONS
        ]
        db.add_all(maisons)

        professeurs = [
            Professeur(nom_prof=nom, anciennete=anciennete)
            for nom, anciennete in PROFESSEURS
        ]
        db.add_all(professeurs)

        cours = [
            Cours(
                nom=nom,
                annee=annee,
                capacite=capacite,
                responsable=professeurs[idx_prof].nom_prof,
                professeur=professeurs[idx_prof],
            )
            for nom, annee, capacite, idx_prof in COURS
        ]
        db.add_all(cours)

        eleves = []
        for i, nom in enumerate(NOMS_ELEVES):
            eleves.append(
                Eleve(
                    nom=nom,
                    annee=(i % 7) + 1,
                    familier=FAMILIERS[i % len(FAMILIERS)],
                    status=StatutEleve.ACTIF,
                    maison=maisons[i % len(maisons)],
                )
            )
        db.add_all(eleves)
        db.flush()

        utilisateurs = []

        for e in eleves:
            utilisateurs.append(
                Utilisateur(
                    email=f"{_slug(e.nom)}.{e.id}@academie.magie",
                    mot_de_passe=MOT_DE_PASSE,
                    role=RoleUser.ELEVE,
                    eleve_id=e.id,
                )
            )

        for p in professeurs:
            utilisateurs.append(
                Utilisateur(
                    email=f"{_slug(p.nom_prof)}.{p.id}@academie.magie",
                    mot_de_passe=MOT_DE_PASSE,
                    role=RoleUser.PROFESSEUR,
                    professeur_id=p.id,
                )
            )

        utilisateurs.append(
            Utilisateur(
                email="admin@academie.magie",
                mot_de_passe=MOT_DE_PASSE,
                role=RoleUser.ADMIN,
            )
        )

        db.add_all(utilisateurs)
        # get_db() commit automatiquement à la sortie du bloc.

    total_users = len(NOMS_ELEVES) + len(PROFESSEURS) + 1
    print("[OK] Seed terminé :")
    print(f"     - {len(MAISONS)} maisons")
    print(f"     - {len(PROFESSEURS)} professeurs")
    print(f"     - {len(COURS)} cours")
    print(f"     - {len(NOMS_ELEVES)} élèves")
    print(f"     - {total_users} utilisateurs (dont 1 admin)")
    print()
    print(f"Comptes de test (mot de passe commun : '{MOT_DE_PASSE}') :")
    print("     admin    -> admin@academie.magie")
    print("     élève    -> prénom.id@academie.magie (ex. elara.1@academie.magie)")


if __name__ == "__main__":
    seed()