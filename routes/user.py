
# Python
import email
from typing import  List
from uuid import UUID
# FastAPI
from fastapi import Body, FastAPI,status
from fastapi import APIRouter,HTTPException
from fastapi import Path
from sqlalchemy.orm.exc import NoResultFound
# Models
import models.user
from schemas.user import User, UserRegister
# Database
from config.database import SessionLocal

# Session
db = SessionLocal()
# Users
user = APIRouter()

# Paths
## Show Users
@user.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
)
def show_all_users():    
    """
    Show All Users

    This path operation show all users in the app

    Parameters:
    -

    Returns a json list with all users in the app, with the following keys
    - user_id: UUID
    - email: str
    - first_name: str
    - last_name: str
    - birth_date: str
    """
    try:
        users = db.query(models.user.User).all() 
    except NoResultFound as err:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Resource not Found")
    
    db.close()
    return  users
## Show a user
@user.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User"
    )
def show_a_user(user_id: UUID = Path(
        ...,
        title= "Tweet Id",
        description="This is the user ID",        
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )):
    """
    Show a User

    This path operation show a user in the app

    Parameters:
        - Request body parameter:
            - user_id: User id
            
    Return a json with the basic user information :
        - user_id: UUID 
        - content: str
        - created_at: datetime 
        - updated_at: Optional[datetime]
        - by: User 
    """  
    user=db.query(models.user.User).filter(models.user.User.user_id==user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Resource not Found")
    return user
## Create user
@user.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User"
)
def signup(user:UserRegister=Body(...)):
    """
    Signup a user

    This path operation registrer a user in the app

    Parameters:
        - Request body parameter:
            - **user: UserRegister**-> Users

    Return a json with the basic information :
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birthday: date
    """  
    db_user = db.query(models.user.User).filter(models.user.User.email==user.email).first()
    if db_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists!")

    new_user=models.user.User(
    user_id=user.user_id,
    email=user.email,
    password= user.password,
    first_name = user.first_name,
    last_name = user.last_name,
    birth_date =user.birth_date
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
## Update user
@user.put(
    path="/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User"   
)
def update_a_user(
    user_id: UUID = Path(
        ...,
        title= "User Id",
        description="This is the User Id",        
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ),
    user: User= Body(...)):
    """
    Update a User

    This path operation updated a user in the app

    Parameters:
        - Request body parameter:
            - usert: User
            
    Return a json with the basic user information :
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """    
    user_to_update=db.query(models.user.User).filter(models.user.User.user_id==user_id).first()    
    user_to_update.email = user.email
    user_to_update.first_name = user.first_name
    user_to_update.last_name = user.last_name
    user_to_update.birth_date = user.birth_date
    
    db.commit()

    return user_to_update
## Delete user
@user.delete(
    path="/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User"
)
def delete_a_user(user_id: UUID = Path(
        ...,
        title= "User Id",
        description="This is the tweet ID",        
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )):
    """
    delete a User

    This path operation delete a user in the app

    Parameters:
        - Request body parameter:
            - user_id: user_id id
            
    Return a json with the basic tweet information :
        - user_id: UUID 
        - content: str
        - created_at: datetime 
        - updated_at: Optional[datetime]
        - by: User 
    """    
    user_to_delete= db.query(models.user.User).filter(models.user.User.user_id==user_id).first()   

    if user_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Resource not Found")

    db.delete(user_to_delete)
    db.commit()

    return user_to_delete
