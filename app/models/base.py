"""
  created by IAmFiveHigh on 2019-02-20
 """

from sqlalchemy import Column, SmallInteger, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    createTime = Column('create_time', DateTime)
