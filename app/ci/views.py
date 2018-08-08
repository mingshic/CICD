#-*- coding: utf-8 -*-

from . import ci
from .runner import source_
# import time
# import hashlib
# import time
import os
# from .. import socketio
from flask import redirect,render_template,request,url_for,session,jsonify,make_response
# from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, Source, Ci_job_artifacts, Ci_job_log
import json
from ..utils import login_request


def data_format_deal(data):
    try:
        if "'" in data:
            data = data.replace("'",'"')
    except:
        pass
    return data

@ci.route('/test', methods=['GET', 'POST'])
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

@ci.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'GET':
        data = os.popen("python app/ci/test.py")
        print (data)
        return "GET style"
    else:
        return "GET style"


@ci.route('/source', methods=['POST', 'GET'])
@login_request.check_login
def source(*args, **kw):
    if request.method == "GET":
        datas = []
        source_ = Source.query.filter(Source.username == kw["username"]).all()
        for num in range(len(source_)):
            data = []
            info = source_[num]
            data.append(info.source.split("/")[-1][:-4])
            data.append(info.id)
            datas.append(data)
        try:
            latest = source_.pop()
            datas.append(latest.source)
            datas.append(latest.id)
        except:
            pass
        return make_response(jsonify(datas))
    if request.method == "POST":
        data = []
        item = request.values.get("item")
        idtoInfo = Source.query.filter(Source.id == item.split("_")[1]).all()[0]
        data.append(idtoInfo.source)
        return make_response(jsonify(data))


@ci.route('/ci_code', methods=['POST', 'GET'])
@login_request.check_login
def ci_code(*args, **kw):
    if request.method == "GET":
        datas = []
        ci_code_ = Ci_job_artifacts.query.filter(Ci_job_artifacts.username == kw["username"]).all()
        for num in range(len(ci_code_)):
            data = []
            info = ci_code_[num]
            data.append(info.job_name)
            data.append(info.jobs)
            data.append(info.id)
            datas.append(data)
        try:
            latest = ci_code_.pop()
            datas.append(latest.jobs)
            datas.append(latest.job_name)
            datas.append(latest.id)
        except:
            pass
        print (datas)
        return make_response(jsonify(datas))
    if request.method == "POST":
        data = []
        item = request.values.get("item")
        idtoInfo = Ci_job_artifacts.query.filter(Ci_job_artifacts.id == item.split("_")[1]).all()[0]
        data.append(idtoInfo.job_name)
        data.append(idtoInfo.jobs)
        return make_response(jsonify(data))


@ci.route('/runner', methods=['POST','GET'])
@login_request.check_login
def runner(*args, **kw):
    if request.method == "POST":
        item = request.values.get("item")
        source = request.values.get('source')
        job_artifacts = request.values.get('job_artifacts')
        job_artifacts_filename = request.values.get('job_artifacts_filename')
        log_directory = request.values.get('log_directory')
        source_directory = request.values.get('source_directory')

        private_dir_name = kw["username"]
        if item == "1":
            _, job_artifacts_filename, log_directory, source_directory = source_(item, source, private_dir_name, job_artifacts, job_artifacts_filename, log_directory, source_directory)
            return make_response(jsonify({"job_artifacts_filename": job_artifacts_filename, "log_directory": log_directory, "source_directory": source_directory}))
        elif item == "2":
            source_(item, source, private_dir_name, job_artifacts, job_artifacts_filename, log_directory, source_directory)
            return make_response(jsonify({"data": "ok"}))

        return make_response(jsonify({"data": "ok"}))



@ci.route('/ci_jobs', methods=['POST','GET'])
@login_request.check_login
# @socketio.on('connect', namespace='/test')
def ci_jobs(*args, **kw):
    if request.method == "GET":
        # resource = []
        page = request.args.get('page', 1, type=int)
        pagination = Ci_job_log.query.order_by(Ci_job_log.username.desc()).paginate(page, per_page=4, error_out=False)
        # for line in range(len(pagination.items)):
        #     res = []
        #     res.append(eval(pagination.items[line].resource))
        #     res.append(pagination.items[line].id)
        #     res.append(pagination.items[line].alias)
        #     resource.append(res)
        return render_template('ci.html', **locals())
        # return render_template('machine.html', name=current_user.username,users=users,pagination=pagination)
    # return render_template('machine.html', pagination=pagination, resource=resource)
    return render_template('ci.html', **locals())


@ci.route('/job', methods=['POST','GET'])
@login_request.check_login
# @socketio.on('connect', namespace='/test')
def job(*args, **kw):
    if request.method == "POST":
        log_directory = request.values.get('log_directory')
        # job_path = Ci_job_log.query.filter(Ci_job_log.log_path == log_directory).first()
        if os.getcwd() == "/home/mingsc/cmdb/jobs/runner/mingsc/ed875ced324a17a2ef01f4ba07a49a31/test":
            file_id = os.getcwd().split("/")[-2]
            # socketio.emit('message', {'data': open("/home/mingsc/cmdb/jobs/runner/mingsc/"+"job_log/"+file_id+"/"+"job.log").readlines()}, namespace='/test')

        # return render_template('socket.html', **locals())
        return redirect(url_for("socket.html"))
        # return make_response(jsonify({"data": "111111"}))
    # return render_template('vueci.html', **locals())
    # socketio.emit('message', {'data': 'This is data', 'time': open("job.log").readlines()},namespace='/test')
    # socketio.emit('message', {'data': open("job.log").readlines()}, namespace='/test')
    if request.method == "GET":
        log = ""
        log_directory = request.values.get('log_directory')
        # print (log_directory)
        # socketio.emit('message', {
        #     'data': open(log_directory + "/" + "job.log").readlines()},
        #           namespace='/test')
        with open(log_directory+"/"+"job.log") as rp:
            log = rp.read().split("\n")
        # return render_template('socket.html', **locals())
        print (len(log))
        return make_response(jsonify({"log": log}))



@ci.route('/ci', methods=['POST','GET'])
@login_request.check_login
def ci(*args, **kw):
    if request.method == "POST":
        item = request.values.get("item")
        # host = request.form.get('ci.host')
        # mode_parameter = request.form.get('mode_parameter')
        source = request.values.get('source')

        ci_jobs = request.values.get('jobs')
        if source:
            if str(item) == "1":
                source_ = source.split("\n")[0]
                insert_source = Source(username=kw["username"],source=source_)
                print (1111111111111111111111111111111111111111111111222222222222222222222222222222)
                db.session.add(insert_source)
                db.session.commit()
                db.session.close()
                # return make_response(jsonify({"log": "log"}))
            elif str(item) == "2":
                if_update = request.values.get('if_update')
                id_ = request.values.get('id').split("_")[1]
                if if_update == "true":
                    source = source.split("\n")[0]
                    update_source = Source.query.filter(Source.id == id_).first()
                    update_source.source = source
                    db.session.commit()
                    db.session.close()
                elif if_update == "false":
                    delete_source = Source.query.filter(Source.id == id_).first()
                    db.session.delete(delete_source)
                    db.session.commit()
                    db.session.close()

        elif ci_jobs:
            if str(item) == "1":
                job_name = request.values.get('job_name')
                ci_jobs_ = ci_jobs.split("\n")
                _ci_jobs = "\n".join(ci_jobs_)
                insert_job_artifacts = Ci_job_artifacts(username=kw["username"],job_name=job_name,jobs=_ci_jobs)
                db.session.add(insert_job_artifacts)
                db.session.commit()
                db.session.close()
            elif str(item) == "2":
                if_update = request.values.get('if_update')
                id_ = request.values.get('id').split("_")[1]
                if if_update == "true":
                    job_name = request.values.get('job_name')
                    ci_jobs = ci_jobs
                    update_job_artifacts = Ci_job_artifacts.query.filter(Ci_job_artifacts.id == id_).first()
                    update_job_artifacts.job_name = job_name
                    update_job_artifacts.jobs = ci_jobs
                    db.session.commit()
                    db.session.close()
                elif if_update == "false":
                    delete_job_artifacts = Ci_job_artifacts.query.filter(Ci_job_artifacts.id == id_).first()
                    db.session.delete(delete_job_artifacts)
                    db.session.commit()
                    db.session.close()

        return redirect(url_for('ci.ci_jobs'))
        # return render_template('ci.html', **locals())
    else:
        try:
            source_ = Source.query.filter(Source.id == 1).first().source
        except:
            source_ = ""
        try:
            ci_jobs_ = Ci_job_artifacts.query.filter(Ci_job_artifacts.id == 1).first().jobs
        except:
            ci_jobs_ = ""
        return render_template('ci.html', **locals())







## @ci.route('/hosts', methods=['POST','GET'])
## @check_login
## def hosts(*args, **kw):
##     form = hostList()
##     if request.method == "POST":
##         body = request.form.get('body')
##
##         # with open("app/ansible_api/hosts", "r") as rp:
##         #     host_info = rp.read()
##         hostlist = hostArticle(body=str(body.split("\r\n")))
##
##         db.session.add(hostlist)
##         db.session.commit()
##         db.session.close()
##         print(hostlist)
##
##         return redirect(url_for('machine.obtain'))
##     else:
##         return render_template("release_deployment.html", form=form)
#
#
#
#
#@ci.route('/machine', methods=['POST', 'GET'])
#@login_request.check_login
#def machine(*args, **kw):
#    if request.method == 'GET':
#        resource = []
#        page = request.args.get('page', 1, type=int)
#        pagination = hostTable.query.order_by(hostTable.id.desc()).paginate(page, per_page=20, error_out=False)
#        for line in range(len(pagination.items)):
#            res = []
#            res.append(eval(pagination.items[line].resource))
#            res.append(pagination.items[line].id)
#            res.append(pagination.items[line].alias)
#            resource.append(res)
#        return render_template('machine.html', **locals())
#        # return render_template('machine.html', name=current_user.username,users=users,pagination=pagination)
#    # return render_template('machine.html', pagination=pagination, resource=resource)
#    return render_template('machine.html', **locals())
#
#

