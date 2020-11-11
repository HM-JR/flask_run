# flask-
第一天 2020/10/23


在tools下的ModelCreate.py下创建你的表：
    1.创建db.Model的子类
    2.运行脚本ModelCreate.py
    3.检查数据库中是否生成表

使用类直接操作数据库
-- ----------------------------------------------
    关于使用model操作数据库的一些方法
    # 插入一条角色数据
    # role1 = user(users='admin',password='adminadmin')
    # db.session.add(role1) 添加一条数据
    # db.session.add_all([role1,role2]) 添加多条数据
    # db.session.commit()

    # a=user.query.first() 第一条数据
    # a = user.query.all() 所有数据
    # a = user.query.filter_by(users = 'admin').all() 按条件查找到的所有数据
    # a = user.query.filter_by(users = 'admin').first() 按条件查找到的第一条数据
    # a = user.query.filter(user.users.endswith('n')).first() 模糊查询
    # a = user.query.get(2)  按照主键的值查询
    # filter(and_(,)) 条件和
    # filter(or_(,)) 条件或
    # filter(not_()) 条件相反


对应的在mysql数据库字段类型

类型名|python中类型|说明
---|:--:|---:
Integer|int|普通整数，一般是32位
SmallInteger | int | 取值范围小的整数，一般是16位
BigInteger |int或long | 不限制精度的整数
Float | float | 浮点数
Numeric | decimal.Decimal |普通整数，一般是32位
String | str | 变长字符串
Text | str | 变长字符串，对较长或不限长度的字符串做了优化
Unicode | unicode | 变长Unicode字符串
UnicodeText | unicode | 变长Unicode字符串，对较长或不限长度的字符串做了优化
Boolean | bool | 布尔值
Date | datetime.date | 时间
Time | datetime.datetime | 日期和时间
LargeBinary | str | 二进制文件
