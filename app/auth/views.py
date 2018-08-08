#-*- coding: utf-8 -*-

from . import auth
from .. import db,admin_permission
from ..models import User
from flask import redirect,render_template,request,url_for,flash
from flask_login import login_user,logout_user,current_user,login_required
# from flask_security import roles_required,current_user,logout_user,login_user,login_required
from flask_principal import Identity, AnonymousIdentity, identity_changed, current_app,IdentityContext



#上下文处理,可以在jinja2判断是否有执行权限
@auth.app_context_processor
def context():
    admin= IdentityContext(admin_permission)
    return dict(admin=admin)

#登录
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        check = request.form.get('check')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password_hash(password):
            if check:
                login_user(user,remember=True)
            else:
                login_user(user)
            #登录时的身份变化
            identity_changed.send(
                current_app._get_current_object(),
                identity=Identity(user.id))
            return redirect(url_for('main.index'))
        else:
            flash("账户或密码错误！")
    return render_template('login.html')

#注销
@auth.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    #注销后身份变成匿名
    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity())
    return redirect(url_for('auth.login'))


#增加用户
@auth.route('/adduser',methods=['GET','POST'])
@login_required
@admin_permission.require(http_exception=403)
def adduser():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        search = User.query.filter_by(username=username).first()
        if search is None:
            user = User(username=username,password=password)
            db.session.add(user)
            db.session.commit()
            flash('应该是提交成功了吧。')
        else:
            flash('这个用户名应该是有人用了吧。。')

    return render_template('adduser.html')
