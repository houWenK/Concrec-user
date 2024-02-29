# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年09月27日
@file:      engine.py
"""

from configparser import ConfigParser
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 获取，解析配置文件
config = ConfigParser()
config.read("./config.ini", encoding="utf-8")

# 创建引擎
# engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}"
#                        .format(quote(config.get("db", "user")), quote(config.get("db", "password")),
#                                config.get("db", "host"), config.get("db", "port"), config.get("db", "database")))

# 创建引擎 mysql5.5以下
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8"
                       .format(quote(config.get("db", "user")), quote(config.get("db", "password")),
                               config.get("db", "host"), config.get("db", "port"), config.get("db", "database")))

# 创建Session类
Session = sessionmaker(bind=engine)

