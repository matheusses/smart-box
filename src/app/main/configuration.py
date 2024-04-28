from src.app.infrastructure.db.engine import Base, engine, get_db

def configure_db() -> None:
    Base.metadata.bind = get_db()
    Base.metadata.create_all(engine)