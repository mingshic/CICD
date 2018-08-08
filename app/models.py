#!/usr/bin/env python3
#-*- coding: utf8 -*-

import time
import datetime
from .config import Tables
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash#转换密码用到的库

db = SQLAlchemy()

class pushTable(db.Model):
    __tablename__ = Tables['push_table']
    push_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    push_host = db.Column(db.String(50))
    # mode_parameter = db.Column(db.Text)
    push_mode = db.Column(db.Text)
    push_parameter = db.Column(db.Text)
    push_response = db.Column(db.String(100))
    push_time = db.Column(db.DateTime, default=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __repr__(self):
        return '%r,%r,%r' % (self.username,self.push_host,self.mode_parameter)
        
class hostArticle(db.Model):
    __tablename__ = "ansible_host"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    identity = db.Column(db.String(100))
    hostlist = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __repr__(self):
        return '%r,%r,%r' % (self.username,self.identity,self.hostlist)



class commandParameterTable(db.Model):
    __tablename__ = "command_parametertable"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    scene = db.Column(db.String(100))
    command_para = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __repr__(self):
        return '%r,%r,%r' % (self.username,self.scene,self.command_para)

class Source(db.Model):
    __tablename__ = "code_source"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(1000))
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __repr__(self):
        return '%r,%r' % (self.username,self.source)


class Ci_job_artifacts(db.Model):
    __tablename__ = "ci_job_artifacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    job_name = db.Column(db.String(100))
    jobs = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __repr__(self):
        return '%r,%r,%r' % (self.username,self.stages,self.content)


class Ci_job_log(db.Model):
    __tablename__ = "ci_job_log"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    job_id = db.Column(db.Integer, autoincrement=True)
    log_path = db.Column(db.String(1000))
    source = db.Column(db.String(1000))
    # stages = db.Column(db.Text)
    # content = db.Column(db.Text)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __repr__(self):
        return '%r,%r,%r,%r' % (self.username,self.job_id,self.log_path,self.source) #,self.stages,self.content)


class hostTable(db.Model):
    __tablename__ = "host_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alias = db.Column(db.String(100))
    resource = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
#    host = db.Column(db.String(1000))
#    platform = db.Column(db.String(1000))
#    cpu = db.Column(db.String(1000))
#    mem = db.Column(db.String(1000))
#    swap = db.Column(db.String(1000))
#    disk = db.Column(db.String(1000))
#    net = db.Column(db.String(1000))
#    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __repr__(self):
        return '%r' % (self.resource)

    
class User(db.Model):
    __tablename__ = 'opm_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(40))
    create_time = db.Column(db.DateTime)
    group_name = db.Column(db.String(50))
    message_num = db.Column(db.Integer)
#    email = db.Column(db.String(40), nullable=False)
#    create_time = db.Column(db.DateTime, nullable=False)
#    group_name = db.Column(db.String(50), nullable=False)
#    message_num = db.Column(db.Integer)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __init__(self, username, password, message, email):
        self.username = username
        self.password = password
        self.email = email
        self.message = message

    def __repr__(self):
        return '<User %r>' % self.username


class Group(db.Model):
    __tablename__ = 'opm_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupname = db.Column(db.String(50), nullable=False, unique=True)
#    user_id = db.Column(db.Integer, db.ForeignKey('opm_user.id'))
    user_id = db.Column(db.Integer)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __repr__(self, groupname):
        return '<Group %r>' % self.groupname


class Message_status(db.Model):
    __tablename__ = 'opm_message_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    send_user = db.Column(db.String(50), nullable=False, unique=True)
    recv_user = db.Column(db.String(50), nullable=False, unique=True)
    send_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __init__(self, send_user, recv_user, send_time, send_text):
        self.send_user = send_user
        self.recv_user = recv_user
        self.send_time = send_time
        self.send_text = send_text

    def __repr__(self, send_user):
        return '<Message %r>' % self.send_user


class Ticket_type(db.Model):
    __tablename__ = 'opm_ticket_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(50), nullable=False, unique=True)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __init__(self, type_name):
        self.type_name = type_name

    def __repr__(self, type_name):
        return '<Ticket_type %r>' % self.type_name


class Ticket(db.Model):
    __tablename__ = 'opm_ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_sn = db.Column(db.String(20), nullable=False, unique=True)
    ticket_type = db.Column(
        db.String(50), db.ForeignKey('opm_ticket_type.type_name'))
    ticket_name = db.Column(db.String(50), nullable=False)
    create_user = db.Column(db.String(50), nullable=False)
    recv_user = db.Column(db.String(50), nullable=False)
    ticket_text = db.Column(db.String(255), nullable=False)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __init__(self, ticket_sn, ticket_type, ticket_name, create_user,
                 recv_user, ticket_text):
        self.ticket_sn = ticket_sn
        self.ticket_type = ticket_type
        self.ticket_name = ticket_name
        self.create_user = create_user
        self.recv_user = recv_user
        self.ticket_text = ticket_text

    def __repr__(self, send_user):
        return '<Message %r>' % self.send_user


class Role(db.Model):
    __tablename__ = 'roles_test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User_test', backref='role')
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __repr__(self):
        return '<Role %s>' % self.name


class User_test(db.Model):
    __tablename__ = 'users_test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles_test.id'))
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def __repr__(self):
        return '<User_test %s>' % self.name

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
