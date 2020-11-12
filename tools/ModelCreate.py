import sys,os
sys.path.append('../')
from tools.Fmodel import db
import logging
logdir = './log'
try:
    os.mkdir(logdir)
except Exception as e:
    pass




class user(db.Model):
    # 定义表名
    __tablename__ = 'AdminUser'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    users = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))

class NormalUser(db.Model):
    # 创建普通用户
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255))
    users = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    prefer = db.Column(db.String(255))
    food = db.relationship('Food', backref='user')

class Food(db.Model):
    __tablename__ = 'Food'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(255))
    palce = db.Column(db.String(255))
    good = db.Column(db.Integer(),default = 0)
    bad = db.Column(db.Integer(),default = 0)
    price = db.Column(db.Float())
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))





if __name__ == '__main__':
    # 创建表格
    db.create_all()


