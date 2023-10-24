from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your PostgreSQL database URL
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Create a database connection instance
database = Database(DATABASE_URL)

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base for defining SQLAlchemy models
Base = declarative_base()
