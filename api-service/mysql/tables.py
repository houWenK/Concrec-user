# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年09月27日
@file:      tables.py
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, DECIMAL

Base = declarative_base()


class Consumer(Base):
    """
    编制类型表的ORM模型
    """
    # 表名
    __tablename__ = "consumer"
    # 数据表中字段名，类型
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    sex = Column(Integer)
    phone_num = Column(String(15))
    email = Column(String(30))
    birth = Column(DateTime)
    introduction = Column(String(255))
    location = Column(String(255))
    avator = Column(String(255))
    create_time = Column(DateTime)
    update_time = Column(DateTime)



