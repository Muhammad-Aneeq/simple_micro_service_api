from dotenv import load_dotenv
from sqlmodel import Field,SQLModel,create_engine,Session
import os
from typing import Optional
load_dotenv() #loading env variables

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = Session(engine)

class Product(SQLModel, table=True):
    id : Optional[int] =  Field(default=None, primary_key=True)
    name : str
    price : str
    quantity:int



# https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e
SQLModel.metadata.create_all(engine)
# // creating tables in database