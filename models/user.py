from uuid import UUID
from sqlalchemy import(
    Column,String,Date
)
from sqlalchemy.orm import relationship

from config.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)

