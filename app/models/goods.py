"""
  created by IAmFiveHigh on 2019-02-20
 """
from app.models.base import Base
from sqlalchemy import Column, SmallInteger, Integer, String, DECIMAL, DateTime, Text, Float


class Good(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(200))
    descr = Column(String(500))
    oldPrice = Column(DECIMAL)
    nowPrice = Column(DECIMAL)
    lowerPrice = Column(String(1000))
    activityEndTime = Column(DateTime)
    tags = Column(String(500))
    tagIds = Column(String(500))
    step = Column(String(500))
    content = Column(Text)
    params = Column(Text)
    images = Column(String(1000))
    icon = Column(String(500))
    innerIcon = Column(String(500))
    liTags = Column(String(500))
    shareTitle = Column(String(500))
    shareDescr = Column(Text)
    shareIcon = Column(String(500))
    accident = Column(String(500))
    sort = Column(Integer)
    safExplain = Column(Text)
    bargainMoney = Column(DECIMAL)
    bargainPercent = Column(Float)
    bargainNum = Column(Integer)
    bargain = Column(Integer)
    bargainSelect = Column(Integer)
    shareLink = Column(String(255))
    shareOpen = Column(Integer)
    tagSafe = Column(String(500))
    saleCount = Column(Integer)
