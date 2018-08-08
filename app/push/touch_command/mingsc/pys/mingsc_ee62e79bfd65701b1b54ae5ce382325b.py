#-*- coding: utf-8 -*-
import os,sys
sys.path.append('/home/mingsc/cmdb')
from app.ansible_api.api import Ansible_api
ansible_api = Ansible_api(['/tmp/mingsc_78b120cc5ab76e0ee0b8d7748edbdd4a.yaml'])
