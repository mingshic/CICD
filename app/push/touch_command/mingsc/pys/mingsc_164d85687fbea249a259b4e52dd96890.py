#-*- coding: utf-8 -*-
import os,sys
sys.path.append('/home/mingsc/cmdb')
from app.ansible_api.api import Ansible_api
ansible_api = Ansible_api(['/tmp/mingsc_055e3b1a2f4c514598d51367df7c9ed0.yaml'])
