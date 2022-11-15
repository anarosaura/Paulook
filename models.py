from sqlalchemy import Column, Integer, String, DateTime
from database import Base

# Este script define el esquema de la base de datos, como las tablas


class Post(Base):
    __tablename__ = "Posts"

    post_id = Column(Integer, primary_key=True, index=True)
    title_post = Column(String)
    user_id = Column(String)
    description = Column(String)
    n_likes = Column(Integer)
    creation_date = Column(String)


class User(Base):
    __tablename__ = "Users"

    user_id = Column(String)
    user_name = Column(String)
    user_age = Column(Integer)
    rol_id = Column(String)
    career = Column(String)
    semester = Column(Integer)
    friends_list = Column(String)


class Rol(Base):
    __tablename__ = "Rol"

    rol_id = Column(Integer, primary_key=True, index=True)
    rol_description = Column(String)