# -*- coding: utf-8 -*-
"""
Created on Thu Mar  16 11:26:05 2020

# Object-relational mapping con SQLALCHEMY - https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

@author: manoel.alonso
"""

#DECLARANDO EL OBJECTO - Object-relational mapping
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#EXTENDENDO EL OBJECTO Base EN UN OBJECTO LLAMADO User
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(80))

#CREANDO UNA CONEXIÓN CON EL MOTOR DE BASE DE DATOS, PUEDE SER CUALQUIERA SQL Server, MySql, Posgres, etc...
from sqlalchemy import create_engine
engine = create_engine('sqlite:///./database.db')


#CASO LA TABLA NO EXISTA, EJECUTAMOS create_all PARA CREARLA
Base.metadata.create_all(engine)
   
#CREAMOS UNA SESIÓN PARA PODER INSERTAR, ACTUALIZAR Y BORRAR DATOS.
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)
session = DBSession()

#INSERTANDO UN USUARIO. 
user1 = User(username='manoel',
             email='manoelgadi@gmail.com',
             password='12345678')    

session.add(user1)
session.commit()

#INSERTANDO OTRO USUARIO. 
user2 = User(username='manoel2',
             email='manoelgadi2@gmail.com',
             password='12345678')    
session.add(user2)
session.commit()

#HACIENDO UN SELECT - EQUIVALENTE A
"""
SELECT id, username, email, password FROM users WHERE users.id = 1
"""
print(session.query(User).filter(User.id == 1))
user = session.query(User).filter(User.id == 1).first()
print("id = {}, username = {}, email = {} ".format(user.id,user.username,user.email))

#UPDATE
user.username='nombre_usuario_cambiado'
session.commit()

#DELETE
session.delete(user)
session.commit()



#CLOSING SESSION
session.close()