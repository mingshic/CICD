#-*- coding: utf-8 -*-

import json
from api import Ansible_api

class AnsiInterface(Ansible_api):
    def __init__(self, resource, *args, **kwargs):
        super(Ansible_api, self).__init__(resource, *args, **kwargs)

    def copy_file(self, host_list, src=None, dest=None):
        """
        copy file
        """
        module_args = "src=%s  dest=%s"%(src, dest)
        self.run(host_list, 'copy', module_args)
        result = self.get_result()
        return self.deal_result(result)

    def git_(self, host_list, repo=None, dest=None, archive=None):
        """
        copy file
        """
        module_args = "repo=%s dest=%s archive=%s"%(repo, dest, archive)
        self.run(host_list, 'git', module_args)
        result = self.get_result()
        return self.deal_result(result)

