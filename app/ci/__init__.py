#-*- coding: utf8 -*-


from flask import Blueprint

ci = Blueprint("ci",__name__)

from . import views
