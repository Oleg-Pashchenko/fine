import random
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
import dotenv

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
dotenv.load_dotenv(dotenv_path=parent_dir)
dotenv_values = dotenv.dotenv_values()
dotenv.load_dotenv()

Base = declarative_base()

engine = create_engine(f'postgresql://{dotenv_values["DB_USER"]}:{dotenv_values["DB_PASSWORD"]}'
                       f'@{dotenv_values["DB_HOST"]}:5432/{dotenv_values["DB_NAME"]}')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    last_activity = Column(DateTime, nullable=False)
    money = Column(Integer, nullable=False, default=0)
    orders = relationship('Orders', backref='user')


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_secret_key = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('shopitems.id'), nullable=False)
    shop_item = relationship('ShopItems', back_populates='order')

    def __init__(self):
        self.order_secret_key = random.randint(10000, 100000)


class ShopItems(Base):
    __tablename__ = 'shopitems'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_url = Column(String, nullable=False)
    order = relationship('Orders', back_populates='shop_item')


class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)


class Quizes(Base):
    __tablename__ = 'quizes'
    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
