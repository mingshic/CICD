#encoding:utf-8  
#!/usr/bin/env python

from flask import Flask, render_template
from . import main
from ..utils import login_request

@main.route('/vueci', methods=['POST','GET'])
@login_request.check_login
def vueci(*args, **kw):
    return render_template("vueci.html", **locals() )