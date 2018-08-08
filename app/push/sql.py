#-*- coding: utf-8 -*-

from ..config import Tables

class insert_db:

    @staticmethod
    def insert_push(argv):
        sql  = '''insert into %s (%s,%s,%s) value ('%s','%s','%s') ''' % (Tables['push_table'],Tables['push_field'][1],Tables['push_field'][2],Tables['push_field'][3],argv['push_host'],argv['push_mode'],argv['push_parameter'])
        return sql
