import email
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import(
    Column,
    String,
    Date, 
    create_engine
)
from sqlalchemy.orm import ( sessionmaker)

engine =  create_engine('postgresql://postgres:123456@localhost/twitter')
Base = declarative_base()


# Modelo
class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    birth_date = Column(Date)

    def __str__(self) :
        return self.email

# relacion entre modelos y conexion
Session = sessionmaker(engine)
session=Session()
 
if __name__=="__main__":
    Base.metadata.create_all(engine)
    #Add user
    """ user1 = User(user_id="3fa85f64-5717-4562-b3fc-2c963f66afa9", email="con@test.com")
    session.add(user1)
    session.commit()
    """
    #consulta users
    users = session.query(User).all()
    for user in users:
        print(user)
