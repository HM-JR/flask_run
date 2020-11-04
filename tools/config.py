# 导入配置信息
with open('./config.ini','r') as f:
    config = eval(f.read())

db_config = config['mysql']


if __name__ == '__main__':
    print(db_config)