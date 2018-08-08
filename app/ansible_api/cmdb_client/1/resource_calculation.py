#!/usr/bin/python


import time
import psutil


def getCPUstate(interval=1):  
    return (" CPU: " + str(psutil.cpu_percent(interval)) + "%")      
def getMemorystate():   
        phymem = psutil.virtual_memory()  
        line = "Memory: %5s%% %6s/%s"%(  
            phymem.percent,  
            str(int(phymem.used/1024/1024))+"M",  
            str(int(phymem.total/1024/1024))+"M"  
            )  
        return line      

def poll(interval):      
        tot_before = psutil.net_io_counters()      
        pnic_before = psutil.net_io_counters(pernic=True)      
        # sleep some time      
        time.sleep(interval)      
        tot_after = psutil.net_io_counters()      
        pnic_after = psutil.net_io_counters(pernic=True)      
        # get cpu state      
        cpu_state = getCPUstate(interval)      
        # get memory      
        memory_state = getMemorystate()      
        return (tot_before, tot_after, pnic_before, pnic_after,cpu_state,memory_state)


