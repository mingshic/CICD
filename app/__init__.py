#-*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_socketio import SocketIO
from .models import db
from .config import Mysqlconfig



bootstrap = Bootstrap()

# async_mode = None
# socketio = SocketIO()


# def create_app():
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config.from_object(Mysqlconfig)

bootstrap.init_app(app)
db.init_app(app)
# socketio.init_app(app=app, async_mode=async_mode)





#    from .auth import auth as api_blueprint
#    app.register_blueprint(api_blueprint)    
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
from .push import push as push_blueprint
app.register_blueprint(push_blueprint)
from .machine import machine as machine_blueprint
app.register_blueprint(machine_blueprint)
from .ci import ci as ci_blueprint
app.register_blueprint(ci_blueprint)
#    from .api import api as api_blueprint
#    app.register_blueprint(api_blueprint)    

# return app
