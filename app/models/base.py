"""
  created by IAmFiveHigh on 2019-02-20
 """

from sqlalchemy import Column, SmallInteger, Integer
from flask_sqlalchemy import SQLAlchemy as sq, BaseQuery
from contextlib import contextmanager
from datetime import datetime


class SQLAlchemy(sq):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    # 所有属性转字典
    def serialize(self):
        from sqlalchemy.orm import class_mapper
        columns = [c.key for c in class_mapper(self.__class__).columns]
        kv = {}
        for k in columns:
            if type(k) == str:
                if getattr(self, k):
                    kv[k] = getattr(self, k)
        kv['create_time'] = self.create_datetime
        return dict(kv)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time).strftime("%Y-%m-%d %H:%M:%S")
        else:
            return None