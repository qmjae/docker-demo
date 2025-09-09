import os
import sqlmodel 
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL not set in environment variables")

engine = sqlmodel.create_engine(DATABASE_URL)

#initialize db
def init_db():
    print("Initializing database...")
    SQLModel.metadata.create_all(engine) #create tables based on models
    
#api routes
def get_session():
    with Session(engine) as session: #context manager, automatically closes session after use
        yield session #generator, yields session object

