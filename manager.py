# from flask_script import Manager, Shell
from app import app, db #socketio #create_app,
from app.models import pushTable
from flask_migrate import Migrate,MigrateCommand
from gevent import monkey
from gevent.wsgi import WSGIServer
#from geventwebsocket.handler import WebSocketHandler
from werkzeug.security import generate_password_hash
import random
import string

monkey.patch_all()
app.config.update(
    DEBUG=True
)

# app=create_app()
# migrate = Migrate(app,db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db)

#def add_system_auth(sys_id, asys_id, asys_key):
#    customer = Customer(system_id=sys_id,access_system_id=asys_id,access_system_key=generate_password_hash(asys_key))
#    db.session.add(customer)
#    db.session.commit()
#    db.session.close()
#    connectdb = command_ready()
#    connectdb.storeFile(Tables['access_use'])
# manager.add_command('run', socketio.run(app=app, host='0.0.0.0', port=5000))
 
if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)#, handler_class=WebSocketHandler)
    http_server.serve_forever()
    # manager.run()
#    app.run(host='0.0.0.0', port=5000)
