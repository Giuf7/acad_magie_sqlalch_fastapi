import os
from contextlib import contextmanager
from dotenv import load_dotenv
from sqlalchemy import create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from dal.models import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(delete=False):
    if delete:
        Base.metadata.drop_all(bind=engine)
        print("[INFO] Toutes les tables ont été supprimées.")
    Base.metadata.create_all(bind=engine)
    print("[OK] Tables créées / mises à jour.")


def test_connexion():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("[OK] Connexion établie à la base de données SQLite")
            return True
    except Exception as e:
        print(f"[ERREUR] Connexion impossible : {e}")
        return False


@contextmanager
def get_db():
    """Context manager utilisé par les scripts (seed, startup)."""
    db = session_local()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def get_db_session():
    """Dépendance FastAPI (Depends) : une session par requête."""
    db = session_local()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()