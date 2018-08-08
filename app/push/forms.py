#-*- coding: utf-8 -*-

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, validators, TextAreaField
from wtforms.validators import DataRequired


class PushInfo(FlaskForm):
    push_host = StringField('host',validators=[DataRequired(message="must give")])
    # push_mode = StringField('mode',validators=[DataRequired(message="content must give")])
    # push_parameter = StringField('parameter')
    identity = StringField('identity',validators=[DataRequired(message="must give")])
    scene = StringField('scene',validators=[DataRequired(message="must give")])

    mode_parameter =  TextAreaField('mode_parameter',validators=[DataRequired(message="must give")])

    hostlist = TextAreaField('hostlist',validators=[DataRequired(message="must give")])

    command_para = TextAreaField('commandpara',validators=[DataRequired(message="must give")])
    submit = SubmitField('Submit')

# class hostList(FlaskForm):
#     body = TextAreaField('hostlist')
#     submit_hostlist = SubmitField('Submit')
#
# class commandParameter(FlaskForm):
#     command_para = TextAreaField('hostlist')
#     submit_commandparameter = SubmitField('Submit')