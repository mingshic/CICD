#!/usr/bin/python


from flask import redirect,request,url_for,flash,session
from functools import wraps

def check_login(func):
    @wraps(func)
    def wrapper(*args, **kw):
        if 'login' not in request.full_path:
            if 'username' in session:
                username = session['username']
                data = {'username': username}
                print(data)
                return func(*args, **data)
            else:
                return redirect(url_for('push.login'))

    return wrapper