#-*- coding: utf-8 -*-

from . import machine
from flask import jsonify,make_response,redirect,render_template,request,url_for
from ..models import hostTable, db
import json
from ..utils import login_request

def data_format_deal(data):
    try:
        if "'" in data:
            data = data.replace("'","|?|")
        elif '"' in data:
            data = data.replace('"',"|?|")
    except:
        pass
    return data

#def data_format_deal_dict(data):
#    try:
#        if "|?|" in data:
#            data = data.replace("|?|",'"')
#    except:
#        pass
#    return data

@machine.route('/machineDB', methods=['GET','POST'])
def machineDB(*args, **kw):
    if request.method == 'POST':
        try:
            alias_id = request.values.get("id").split("_")[1]
            alias = request.values.get("alias")
        except:
            pass
        try:
            data = request.data
            data = json.loads(data.decode("utf8"))
        except:
            pass
        if data:
            resour = hostTable.query.filter().all()
            id_ = None
            for rs in range(len(resour)):
                line_rs = eval(resour[rs].resource)
                if line_rs["HOST"]["hostname"] == data["HOST"]["hostname"]:
                    id_ = resour[rs].id
                    break
            if id_ is None:
                insert_host = hostTable(resource=str(data))
                # if data["HOST"]["hostname"] ==
                db.session.add(insert_host)
                db.session.commit()
                db.session.close()
            elif id_:
                update_hostTable = hostTable.query.filter(hostTable.id == id_).first()
                update_hostTable.resource = str(data)
                db.session.commit()
                db.session.close()
        try:
            if alias:
                update_hostTable = hostTable.query.filter(hostTable.id == alias_id).first()
                update_hostTable.alias = alias
                db.session.commit()
                db.session.close()
        except:
            pass


        return render_template('machine.html', **locals())
    else:
        return make_response(jsonify({"code": 1, "data": "avarible"}))


@machine.route('/obtain', methods=['GET','POST'])
def obtain():
    if request.method == 'GET':
        resource = []
        page=request.args.get('page',1,type=int)
        pagination=hostTable.query.order_by(hostTable.id.desc()).paginate(page,per_page=4,error_out=False)
        for line in range(len(pagination.items)):
            res = []
            res.append(eval(pagination.items[line].resource))
            res.append(pagination.items[line].id)
            resource.append(res)

            # return render_template('machine.html', name=current_user.username,users=users,pagination=pagination)
        return render_template('machine.html', pagination=pagination, resource=resource)


@machine.route('/base', methods=['GET', 'POST'])
def base():
    if request.method == 'POST':
        data = request.data
        data = json.loads(data.decode("utf8"))
        insert_host = hostTable(resource=str(data))
        db.session.add(insert_host)
        db.session.commit()
        db.session.close()
        return make_response(jsonify({"code": 1, "data": data}))
    else:
        return render_template('base.html')