#-*- coding: utf-8 -*-

from . import push
import hashlib
import time
import os
from flask import redirect,render_template,request,url_for,session,jsonify,make_response
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import pushTable, User, hostArticle, db, hostTable, commandParameterTable
from .forms import PushInfo
from .run_ansible import Run_ansible
# from ..ansible_api.api import Ansible_api
import json
from ..utils import login_request


def data_format_deal(data):
    try:
        if "'" in data:
            data = data.replace("'",'"')
    except:
        pass
    return data


@push.route('/')
@push.route('/index')
@login_request.check_login
def index(*args, **kw):
    return render_template('index.html', **locals())

@push.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        print (username,password,user.password)
        if user is not None and check_password_hash(user.password,password):
            messages = {
                "code": 200,
                "data": {
                    "status": "success",
                    "info": None
                }
            }
            session['username'] = username
            return redirect(url_for('push.index'))
            # return json.dumps(messages)
        else:
            messages = {
                "code": 200,
                "data": {
                    "status": "failed",
                    "info": "username or password error"
                }
            }
            return json.dumps(messages)
    return render_template("login.html")

@push.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        messages = {
            "code": 200,
            "data": {
                "status": "success",
                "info": None
            }
        }
        # return json.dumps(messages)
        return redirect(url_for('push.index'))
    else:
        return "null"

@push.route('/hostlist', methods=['POST', 'GET'])
@login_request.check_login
def hostlist(*args, **kw):
    if request.method == "GET":
        datas = []
        hostlist_ = hostArticle.query.filter(hostArticle.username == kw["username"]).all()
        for num in range(len(hostlist_)):
            data = []
            info = hostlist_[num]
            identity = info.identity.replace("[","").replace("]","")
            data.append(identity)
            data.append(info.hostlist)
            data.append(info.id)
            datas.append(data)
        try:
            latest = hostlist_.pop()
            datas.append(latest.hostlist)
            datas.append(latest.identity)
            datas.append(latest.id)
        except:
            pass
        return make_response(jsonify(datas))
    if request.method == "POST":
        data = []
        item = request.values.get("item")
        idtoInfo = hostArticle.query.filter(hostArticle.id == item.split("_")[1]).all()[0]
        data.append(idtoInfo.identity)
        data.append(idtoInfo.hostlist)
        return make_response(jsonify(data))


@push.route('/commandPara', methods=['POST', 'GET'])
@login_request.check_login
def commandPara(*args, **kw):
    if request.method == "GET":
        datas = []
        commandPara_ = commandParameterTable.query.filter(commandParameterTable.username == kw["username"]).all()
        for num in range(len(commandPara_)):
            data = []
            info = commandPara_[num]
            scene = info.scene.replace("[", "").replace("]", "")
            data.append(scene)
            data.append(info.command_para)
            data.append(info.id)
            datas.append(data)
        try:
            latest = commandPara_.pop()
            datas.append(latest.command_para)
            datas.append(latest.scene)
            datas.append(latest.id)
        except:
            pass
        return make_response(jsonify(datas))
    if request.method == "POST":
        data = []
        item = request.values.get("item")
        idtoInfo = commandParameterTable.query.filter(commandParameterTable.id == item.split("_")[1]).all()[0]
        data.append(idtoInfo.scene)
        data.append(idtoInfo.command_para)
        return make_response(jsonify(data))

@push.route('/release', methods=['POST','GET'])
@login_request.check_login
def release(*args, **kw):
    form = PushInfo()
    if request.method == "POST":
        item = request.values.get("item")

        # host = request.form.get('push_host')
        # mode_parameter = request.form.get('mode_parameter')

        hostlist = request.values.get('hostlist')


        command_para = request.values.get('command_para')

        print (kw["username"])


        if hostlist:
            if str(item) == "1":
                hostlist = hostlist.split("\n")
                identity = hostlist[0]
                hostlist = "\n".join(hostlist[1:])
                insert_hostlist = hostArticle(username=kw["username"],identity=identity,hostlist=hostlist)
                db.session.add(insert_hostlist)
                db.session.commit()
                db.session.close()
            elif str(item) == "2":
                if_update = request.values.get('if_update')
                id_ = request.values.get('id').split("_")[1]
                if if_update == "true":
                    hostlist = hostlist.split("\n")
                    identity = hostlist[0]
                    hostlist = "\n".join(hostlist[1:])
                    update_hostlist = hostArticle.query.filter(hostArticle.id == id_).first()
                    update_hostlist.identity = identity
                    update_hostlist.hostlist = hostlist
                    db.session.commit()
                    db.session.close()
                elif if_update == "false":
                    delete_hostlist = hostArticle.query.filter(hostArticle.id == id_).first()
                    db.session.delete(delete_hostlist)
                    db.session.commit()
                    db.session.close()

        elif command_para:
            if str(item) == "1":
                scene = request.values.get('scene')
                command_para = command_para.split("\n")
                command_para = "\n".join(command_para)
                insert_commandpara = commandParameterTable(username=kw["username"],scene=scene,command_para=command_para)
                db.session.add(insert_commandpara)
                db.session.commit()
                db.session.close()
            elif str(item) == "2":
                if_update = request.values.get('if_update')
                id_ = request.values.get('id').split("_")[1]
                if if_update == "true":
                    scene = request.values.get('scene')
                    command_para = command_para
                    print(111111111111111111111111111111111111111111111111111111111111111111111)
                    print(id_)
                    print(scene)
                    update_command_para = commandParameterTable.query.filter(commandParameterTable.id == id_).first()
                    update_command_para.scene = scene
                    update_command_para.command_para = command_para
                    db.session.commit()
                    db.session.close()
                elif if_update == "false":
                    delete_command_para = commandParameterTable.query.filter(commandParameterTable.id == id_).first()
                    db.session.delete(delete_command_para)
                    db.session.commit()
                    db.session.close()

        print (1111111111111111111111111111111111111111111111111111111111111111111111)
        return redirect(url_for('push.release'))
    else:

        try:
            hostlist = hostArticle.query.filter(hostArticle.id == 1).first().hostlist
        except:
            hostlist = ""
        try:
            command_parameter = commandParameterTable.query.filter(commandParameterTable.id == 1).first().command_para
        except:
            command_parameter = ""
        return render_template('release_deployment.html', **locals())

@push.route('/deployment', methods=['POST', 'GET'])
@login_request.check_login
def deployment(*args, **kw):
    # form = PushInfo()
    if request.method == "POST":
        host = request.values.get('hostlist')
        mode_parameter = request.values.get('command_para')

        uuid = hashlib.md5()
        uuid.update(bytes(str(time.time()), encoding='utf-8'))
        file_id = uuid.hexdigest()

        host_tempfile = "/tmp/%s_%s.yaml" % (kw["username"],file_id)

        with open(host_tempfile, "w") as wp:
            wp.write(host)

        host = host.split("\n")[0].replace("[","").replace("]","")

        mode_, parameter_ = Run_ansible(host, host_tempfile, mode_parameter, kw["username"])
        print ("qqqqqqqqqqqqqqqqqqqqqqqqqqq %s" % str(mode_))
        print ("qqqqqqqqqqqqqqqqqqqqqqqqqqqeeeeeee %s" % str(parameter_))
        insert_push = pushTable(username=kw["username"], push_host=host, push_mode=str(mode_), push_parameter=str(parameter_))
    # push_mode = str(mode_), push_parameter = str(parameter_)
        db.session.add(insert_push)
        db.session.commit()
        db.session.close()
        os.remove(host_tempfile)

        return make_response(jsonify({"data": "ok"}))
#        return render_template('base/login.html',form=form)
#        return render_template('bootstrap.html',form=form)


# @push.route('/hosts', methods=['POST','GET'])
# @check_login
# def hosts(*args, **kw):
#     form = hostList()
#     if request.method == "POST":
#         body = request.form.get('body')
#
#         # with open("app/ansible_api/hosts", "r") as rp:
#         #     host_info = rp.read()
#         hostlist = hostArticle(body=str(body.split("\r\n")))
#
#         db.session.add(hostlist)
#         db.session.commit()
#         db.session.close()
#         print(hostlist)
#
#         return redirect(url_for('machine.obtain'))
#     else:
#         return render_template("release_deployment.html", form=form)




@push.route('/machine', methods=['POST', 'GET'])
@login_request.check_login
def machine(*args, **kw):
    if request.method == 'GET':
        resource = []
        page = request.args.get('page', 1, type=int)
        pagination = hostTable.query.order_by(hostTable.id.desc()).paginate(page, per_page=20, error_out=False)
        for line in range(len(pagination.items)):
            res = []
            res.append(eval(pagination.items[line].resource))
            res.append(pagination.items[line].id)
            res.append(pagination.items[line].alias)
            resource.append(res)
        return render_template('machine.html', **locals())
        # return render_template('machine.html', name=current_user.username,users=users,pagination=pagination)
    # return render_template('machine.html', pagination=pagination, resource=resource)
    return render_template('machine.html', **locals())


@push.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter_by(username=username).first()
            print (user.username)
            return "POST style"
    else:
        return "GET style"
