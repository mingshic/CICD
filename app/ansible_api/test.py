
from api import Ansible_api

ansible_api = Ansible_api(["./hosts"])
ansible_api.run_adhoc("test01", "shell", "cat /etc/redhat-release")
ansible_api.run_adhoc("test01", "shell", "cat /etc/redhat-release")
ansible_api.run_adhoc("test01", "shell", "cat /etc/redhat-release")
ansible_api.run_adhoc("test01", "shell", "cat /etc/redhat-release")
