# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Fund(Base):
    __tablename__ = 'myfund'

    id = Column(Integer, primary_key=True)
    fcode = Column(String(6), unique=True)
    fname = Column(String(100))
    NAV = Column(Numeric(10, 0))
    ACCNAV = Column(Numeric(10, 0))
    updatetime = Column(DateTime)
