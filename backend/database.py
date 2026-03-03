from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:130096@localhost:3306/client_portal"

engine = create_engine(
    DATABASE_URL,
    pool_size=5,        # number of connections kept ready
    max_overflow=10,    # extra temporary connections
    pool_timeout=30,    # wait time before timeout
    pool_recycle=1800   # refresh connection every 30 mins
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()