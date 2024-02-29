# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年09月30日
@file:      consumer_data.py
"""
from mysql.engine import Session
from mysql.tables import Consumer


def get_consumerByName(username):
    session = Session()
    password = session.query(Consumer.id, Consumer.password, Consumer.avator).filter(
        Consumer.username == username).first()
    session.close()
    return password


def add_consumer(member_information):
    """
      增加人员信息
      无返回
    """
    session = Session()
    p = Consumer(username=member_information["username"],
                 password=member_information["password"],
                 sex=member_information["sex"],
                 phone_num=member_information["phoneNum"],
                 email=member_information["email"],
                 birth=member_information['birth'],
                 introduction=member_information['introduction'],
                 location=member_information['location'],
                 avator=member_information['avator'],
                 create_time=member_information['createTime'],
                 update_time=member_information['updateTime']
                 )
    session.add(p)
    session.commit()
    session.close()


def get_consumerById(id):
    session = Session()
    user = session.query(Consumer.username, Consumer.password, Consumer.sex, Consumer.phone_num, Consumer.email,
                         Consumer.birth, Consumer.introduction, Consumer.location).filter(
        Consumer.id == id).first()
    session.close()
    return user


def update_consumer(member_information):
    session = Session()
    p = session.query(Consumer).filter(Consumer.id == member_information["id"]).first()
    p.username = member_information["username"]
    p.password = member_information["password"]
    p.sex = member_information["sex"]
    p.phone_num = member_information["phoneNum"]
    p.email = member_information["email"]
    p.birth = member_information["birth"]
    p.introduction = member_information["introduction"]
    p.location = member_information["location"]
    p.update_time = member_information["updateTime"]
    session.commit()
    session.close()
