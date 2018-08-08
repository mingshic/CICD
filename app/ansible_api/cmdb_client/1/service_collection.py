#!/usr/bin/python

import os

#def data_format_deal(data):
#    data = data.replace("\n","\?")
#    return data

def proccess_port():
    if os.path.exists("/usr/sbin/ss"):
        ss = os.popen("/usr/sbin/ss -antl |awk -F ' ' '{print $4}'")
    elif os.path.exists("/bin/ss"):
        ss = os.popen("/bin/ss -antl |awk -F ' ' '{print $4}'")
    elif os.path.exists("/usr/bin/ss"):
        ss = os.popen("/usr/bin/ss -antl |awk -F ' ' '{print $4}'")
    ports = ss.read().strip().split("\n")
    _port = []
    
    for port in range(len(ports)):
        port_ = ports[port].split(":")[-1]
        if port_.isdigit():
            _port.append(port_)
    return _port

def inf(where, infos):
    portlist = proccess_port()
    for port in portlist:
        info = ",".join(os.popen("%s -i:%s |awk -F ' ' '{print $1,$9}'|grep -vi name|grep -vi ssh|uniq" % (where, port)).read().strip().split("\n"))
        if info != "":
            infos.update({port: info})
    return infos

def proccess():
    infos = {}
    if os.path.exists("/usr/sbin/lsof"):
        where = "/usr/sbin/lsof"
        infos = inf(where, infos)
        return infos
    elif os.path.exists("/bin/lsof"):
        where = "/bin/lsof"
        infos = inf(where, infos)
        return infos 
    elif os.path.exists("/usr/bin/lsof"):
        where = "/usr/bin/lsof"
        infos = inf(where, infos)
        return infos

    
