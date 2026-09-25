from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative import declarative_base # old import location

SQLALCHEMY_DATABASE_URL = "sqlite:///./todoapp.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={'check_same_thread': False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

'''
engine
=
How do we reach the database?


Base
=
Foundation that lets SQLAlchemy recognize
our model classes as database table definitions


Base.metadata
=
Collection of those table definitions


Base.metadata.create_all(bind=engine)
=
Create those tables in the database


SessionLocal
=
Factory for creating database sessions


SessionLocal()
=
One actual working session


get_db()
=
Usually creates and cleans up one session
for a request
'''