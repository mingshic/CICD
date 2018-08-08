#-*- coding: utf-8 -*-
import os,sys
sys.path.append('/home/mingsc/cmdb')
from app.ansible_api.api import Ansible_api
ansible_api = Ansible_api(['/tmp/mingsc_9bca0ef122587e92733488c2aad4a797.yaml'])
ansible_api.run_adhoc('test02', 'file', 'path=/opt/cmdb_agent state=directory')
ansible_api.run_adhoc('test02', 'unarchive', 'src=/home/mingsc/cmdb/app/ansible_api/cmdb_client/cmdb_agent.tar.gz dest=/opt/cmdb_agent mode="777"')
ansible_api.run_adhoc('test02', 'cron', 'minute=*/1 user=root job="python /opt/cmdb_agent/resource_info.py"')
ansible_api.run_adhoc('test02', 'shell', 'cp -rp /tmp/xx.yaml /opt/xx.yaml')
ansible_api.run_adhoc('test02', 'apt', 'name=lsof state=latest')
ansible_api.run_adhoc('test02', 'apt', 'name=python-pip state=installed')
ansible_api.run_adhoc('test02', 'yum', 'name=lsof state=latest')
ansible_api.run_adhoc('test02', 'yum', 'name=python-pip state=installed')
ansible_api.run_adhoc('test02', 'pip', 'name=psutil')
ansible_api.run_adhoc('test02', 'pip', 'name=ansible')
ansible_api.run_adhoc('test02', 'pip', 'name=requests')
