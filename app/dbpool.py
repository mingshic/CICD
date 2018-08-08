#-*- coding: utf-8 -*-

import pymysql
from .config import Mysql_parameter

class MysqlDB(object):
    def __init__(self):
        self.host = Mysql_parameter['HOST']
        self.port = Mysql_parameter['PORT']
        self.user = Mysql_parameter['USER']
        self.passwd = Mysql_parameter['PASSWD']
        self.db = Mysql_parameter['DB']
        self.charset = Mysql_parameter['CHARSET']

        self.connection

    @property
    def connection(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        conn = conn.cursor()
        return conn
