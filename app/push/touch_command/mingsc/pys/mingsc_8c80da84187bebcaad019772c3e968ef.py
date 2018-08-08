#-*- coding: utf-8 -*-
import os,sys
sys.path.append('/home/mingsc/cmdb')
from app.ansible_api.api import Ansible_api
ansible_api = Ansible_api(['/tmp/mingsc_0fd06985859f4237748e9a80e1f925dd.yaml'])
ansible_api.run_adhoc('test02', 'shell', 'uptime')
