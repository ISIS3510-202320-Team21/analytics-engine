from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/sportpal_db"

# create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# define declarative base
Base = declarative_base()

# reflect current database engine to metadata
metadata = MetaData(engine)
metadata.reflect()

# call the session maker factory
Session = sessionmaker(engine)
db = Session()