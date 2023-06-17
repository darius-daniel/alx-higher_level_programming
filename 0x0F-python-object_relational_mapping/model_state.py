#!/usr/bin/python3
"""
A script that contains the class definition of a State and an instance
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
