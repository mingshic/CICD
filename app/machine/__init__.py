

from flask import Blueprint

machine = Blueprint("machine",__name__,)

from app.machine import views
