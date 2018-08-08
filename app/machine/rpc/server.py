# -*- encoding=utf-8 -*-
from concurrent import futures
import time
import subprocess
import codecs
import sys
import os
 
import grpc
import rpc_pb2
import rpc_pb2_grpc

from ..models import hostTable, db
 
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
#server端文件保存的位置
#jmeter_config = os.path.join(os.getcwd(),'conf/config.jmx')
 
class Performance(rpc_pb2_grpc.RPCServicer):
 
    def sendConfFile(self, content,context):
        ''' 保存配置文件,如config.jmx '''
        text = content.text
        text = eval(text)
        try:
            hostname_ip = eval(text)["HOST"]["hostname"] + "=-=" + eval(text)["HOST"]["ip"]
            
            jmeter_config = os.path.join(os.getcwd(),"data/" + hostname_ip)
            insert_host = hostTable(host=text["HOST"],platform=text["PLATFORM"],cpu=text["CPU"],mem=text["MEM"],swap=text["SWAP"],disk=text["DISK"],net=text["NET"])
            db.session.add(insert_host)
            db.session.commit()
            db.session.close()

            conf_handle = codecs.open(jmeter_config,'w',encoding='utf-8')
            conf_handle.write(text)
            return rpc_pb2.Status(code=0)
        except Exception as e:
            print (e)
            return rpc_pb2.Status(code=1)
 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc_pb2_grpc.add_RPCServicer_to_server(Performance(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
 
 
if __name__ == '__main__':
    serve()
