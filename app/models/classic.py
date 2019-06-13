"""
  created by IAmFiveHigh on 2019-06-05
 """
from .base import Base
from sqlalchemy import Column, SmallInteger, Integer, String


class Classic(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String(200))
    fav_num = Column(Integer)
    image = Column(String(200))
    index = Column(Integer)
    like_status = Column(Integer)
    pubdate = Column(String(100))
    title = Column(String(100))
    type = Column(Integer)
    url = Column(String(200))