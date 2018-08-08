#-*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import pickle

from ..models import MysqlDB
from .sql import insert_db

def data_format_deal(data):
    try:
        if "'" in data:
            data = data.replace("'","")
        elif '"' in data:
            data = data.replace('"',"")
    except:
        pass
    return data

class command_ready(MysqlDB):
    def __init__(self):
        super(command_ready,self).__init__()
        self.conn = self.connection
    def operation_close(self):
        self.conn.connection.commit()
        self.conn.connection.close()
#    def select_union_raw_custsystem(self, deal_status):
#        sql = '''select * from %s, %s where %s.%s=%s.%s and %s.%s=%s.%s and %s.%s=%s.%s and %s.%s='%s' ''' % (Tables["format_table"],Tables["customer_system_table"],Tables["format_table"],"customer_code",Tables["customer_system_table"],"customer_code",Tables["format_table"],"monitor_code",Tables["customer_system_table"],"monitor_code",Tables["format_table"],"monitor_version",Tables["customer_system_table"],"monitor_version",Tables["format_table"],"deal_status",deal_status)
#        conn = self.conn
#        conn.execute(sql)
#        penging_data = conn.fetchall()
#        conn.connection.commit()
#        conn.connection.close()
#        return penging_data

    def insert_push(self, **argv):
        conn = self.conn
        conn.execute(insert_db.insert_push(argv))
        conn.connection.commit()
        conn.connection.close()
        
