from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from settings import DB_URL

# Writer nodes
WRITE_ENGINE: Engine = create_engine(DB_URL, pool_pre_ping=True, pool_size=10)
SESSION: Session = sessionmaker(bind=WRITE_ENGINE)()
USER_MANAGEMENT_SESSION = Session = sessionmaker(bind=WRITE_ENGINE)

async def get_db():
    db = USER_MANAGEMENT_SESSION()
    try:
        yield db
    finally:
        db.close()


def get_db_sync():
    db = USER_MANAGEMENT_SESSION()
    try:
        yield db
    finally:
        db.close()


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        params = {k: v for k, v in kwargs.items()}
        params.update(defaults or {})
        instance = model(**params)
        try:
            session.add(instance)
            session.commit()
        except Exception:  # The actual exception depends on the specific database so we catch all exceptions. This is similar to the official documentation: https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True
