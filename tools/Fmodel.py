import pymysql
from run import app
from flask_sqlalchemy import SQLAlchemy
from tools.config import db_config
pymysql.install_as_MySQLdb()
SQLALCHEMY_DATABASE_URL = 'mysql + pymysql://ljr:123456@192.168.2.219:3306/dataljr'
SQLALCHEMY_TRACK_MODIFICATIONS = True





class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = db_config['user']
    password = db_config['pwd']
    database = db_config['database']
    host = db_config['host']
    port = db_config['port']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (user,password,host,port,database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

app.config.from_object(Config)

db =SQLAlchemy(app)
if __name__ == '__main__':
    print(app.config)