# import urllib.parse
#
# class Config:
#     # 数据库连接信息
#
#     # 对密码进行 URL 编码
#     DB_PASSWORD_ENCODED = urllib.parse.quote(DB_PASSWORD)
#
#     # 数据库配置
#     SQLALCHEMY_DATABASE_URI = (
#         f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}/{DB_NAME}"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False



# import json
# import urllib.parse
# import os
#
# class Config:
#     # 加载配置文件
#     with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
#         config = json.load(config_file)
#
#     # 数据库连接信息
#     DB_USER = config['DB_USER']
#     DB_PASSWORD = config['DB_PASSWORD']
#     DB_HOST = config['DB_HOST']
#     DB_NAME = config['DB_NAME']
#
#     # 对密码进行 URL 编码
#     DB_PASSWORD_ENCODED = urllib.parse.quote(DB_PASSWORD)
#
#     # 数据库配置
#     SQLALCHEMY_DATABASE_URI = (
#         f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}/{DB_NAME}"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
import json
import os
import sys
import urllib.parse

# 获取配置文件路径
basedir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
config_path = os.path.join(basedir, 'config.json')

# 加载配置文件
try:
    with open(config_path) as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print(f"Configuration file not found at {config_path}")
    sys.exit(1)

class Config:
    DB_USER = config['DB_USER']
    DB_PASSWORD = config['DB_PASSWORD']
    DB_HOST = config['DB_HOST']
    DB_NAME = config['DB_NAME']
    DB_PASSWORD_ENCODED = urllib.parse.quote(DB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
