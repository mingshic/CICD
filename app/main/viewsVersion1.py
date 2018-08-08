#encoding:utf-8  
#!/usr/bin/env python

import psutil
import time
from . import main
from threading import Lock
from flask import Flask, render_template
from app import socketio
from subprocess import Popen, PIPE, STDOUT

# thread = None
# thread_lock = Lock()
#
#
# def background_stuff():
# #    p = Popen('python /home/mingsc/cmdb/test.py', stdout=PIPE, stderr=STDOUT, shell=True)
# #    for l in p.stdout:
# #        print (l.strip().decode("utf8"))
# #        socketio.emit('message', {'data': 'This is data', 'time': l.strip().decode("utf8")}, namespace='/test')
#     socketio.emit('message', {'data': 'This is data', 'time': open('job.log').readlines()}, namespace='/test')
#
#
# @main.route('/socket')
# def index():
#     return render_template('socket.html', async_mode=socketio.async_mode)
#
# @socketio.on('connect', namespace='/test')
# def test_connect():
# #    global thread
# #    if thread is None:
# #        thread = Thread(target=background_stuff)
# #        thread.start()
#     socketio.start_background_task(target=background_stuff)
# #    background_stuff()
