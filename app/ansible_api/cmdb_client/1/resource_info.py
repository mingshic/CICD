#!/usr/bin/python

import time
import psutil as ps
import socket
import platform
import requests
from config import url

from service_collection import proccess  
from resource_usage import mem_usage,swap_usage,load_avg,disk_usage,cpu_usage
from resource_calculation import poll

def resouce_coll():
    info_data = {"HOST": {},"PLATFORM": {}, "CPU": {}, "MEM": {}, "SWAP": {}, "DISK": {}, "NET": {}}
    
    #host_info
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    info_data["HOST"]["hostname"] = hostname
    info_data["HOST"]["ip"] = ip
    
    #platform
    info_data["PLATFORM"]["node"] = platform.node()
    info_data["PLATFORM"]["platform"] = platform.platform()
    info_data["PLATFORM"]["processor"] = platform.processor()
    info_data["PLATFORM"]["machine"] = platform.machine()
    info_data["PLATFORM"]["architecture"] = platform.architecture()
    info_data["PLATFORM"]["uname"] = platform.uname()
    
    #cpu
    cpu = ps.cpu_times()
    info_data["CPU"]["cpu_usage"] = ps.cpu_percent(interval = 1)
    info_data["CPU"]["cpu_user"] = cpu.user
    info_data["CPU"]["cpu_system"] = cpu.system
    info_data["CPU"]["cpu_idle"] = cpu.idle
    
    #mem
    mem = ps.virtual_memory()
    info_data["MEM"]["mem_free"] = mem.free
    info_data["MEM"]["mem_used"] = mem.used
    info_data["MEM"]["mem_available"] = mem.available
    info_data["MEM"]["mem_usage"] = mem.percent
    
    #swap
    swap = ps.swap_memory()
    info_data["SWAP"]["swap_total"] = swap.total
    info_data["SWAP"]["swap_used"] = swap.used
    info_data["SWAP"]["swap_free"] = swap.free
    info_data["SWAP"]["swap_free"] = swap.free
    
    #DISK
    disk = ps.disk_io_counters(perdisk=True)
    for prefix in disk.keys():
        info_data["DISK"][prefix + "-" + "read_count"] = disk[prefix].read_count
        info_data["DISK"][prefix + "-" + "write_count"] = disk[prefix].write_count
        info_data["DISK"][prefix + "-" + "read_bytes"] = disk[prefix].read_bytes
        info_data["DISK"][prefix + "-" + "write_bytes"] = disk[prefix].write_bytes
    
    #NET
    net = ps.net_io_counters(pernic=True)
    for prefix in net.keys():
        info_data["NET"][prefix + "-" + "bytes_sent"] = net[prefix].bytes_sent
        info_data["NET"][prefix + "-" + "write_count"] = net[prefix].bytes_recv
        info_data["NET"][prefix + "-" + "read_bytes"] = net[prefix].packets_sent
        info_data["NET"][prefix + "-" + "write_bytes"] = net[prefix].packets_recv
    
    return info_data 

if __name__=="__main__":
    info_data = resouce_coll() 
    service_info = proccess()
    info_data.update({"SERVICE_INFO": service_info})
    mem_usage = mem_usage()
    info_data.update({"MEM_USAGE": mem_usage})
    swap_usage = swap_usage()
    info_data.update({"SWAP_USAGE": swap_usage})
    load_avg = load_avg()
    info_data.update({"LOAD_AVG": load_avg})
    disk_usage = disk_usage()
    info_data.update({"DISK_USAGE": disk_usage})
    cpu_usage = cpu_usage()
    info_data.update({"CPU_USAGE": cpu_usage})
    args = poll(2)
    info_data.update({"UNILIZATION_RATIO": (time.asctime()+" | "+args[4]+" | "+args[5])})
    r = requests.post(url, json=info_data)
