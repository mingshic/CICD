# -*- coding: utf-8 -*-

import os


class Mysqlconfig():

    ENV = 'Mysqlconfig'
    DEBUG = True

    # session
    CSRF_ENABLED = True
    SECRET_KEY = "asgSfsf3Xd8ffy]fw8vfd0zbvssqwertsd4sdwe"

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    use_native_unicode = "utf8"
    
    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://cmdb:123456@localhost/cmdb?charset=utf8"
#    SQLALCHEMY_ECHO = True


#config = {
#    'development': DevelopmentConfig,
#} 

Mysql_parameter = {
    "HOST": "localhost",
    "PORT": 3306,
    "USER": "cmdb",
    "PASSWD": "123456",
    "DB": "cmdb",
    "CHARSET": "utf8",
}

Tables = {
    "push_table": "push_agent", "push_field": ["push_id", "push_host", "push_mode", "push_parameter", "push_response", "push_time"]
}
