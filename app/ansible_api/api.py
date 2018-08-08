#!/usr/bin/env python

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """
    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_on_failed(self, result, *args, **kwargs):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))

    def v2_runner_on_unreachable(self, result):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))


class Ansible_api:
    def __init__(self, hosts):
        self.Options = namedtuple("Options",['connection', 'forks', 'check', 'module_path', 'passwords', 'become', 'become_method', 'become_user', 'listhosts', 'listtasks', 'listtags', 'syntax', 'diff'])
        self.loader = DataLoader()

        self.options = self.Options(connection="smart", forks=5, check=False, module_path=None, passwords=None, become=None, become_method=None, become_user=None, listhosts=None, listtasks=None, listtags=None, syntax=None, diff=False)

        self.passwords = dict(vault_pass='secret')

        self.results_callback = ResultCallback()

        self.inventory = InventoryManager(loader=self.loader, sources=hosts)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        

# Instantiate our ResultCallback for handling results as they come in

# create inventory and pass to var manager
    def run_adhoc(self, host, module, args=""):
        play_source =  dict(
            name = "Ansible Play",
            hosts = host,
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module=module, args=args))#, register='shell_out'),
#                dict(action=dict(module=module, args=dict(msg='{{shell_out.stdout}}')))
             ]
        )
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)
# create play with tasks

# actually run it
        tqm = None
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
             # passwords=passwords,
                passwords=self.passwords,
                stdout_callback=self.results_callback,  # Use our custom callback instead of the ``default`` callback plugin
            )
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()


    def run_playbook(self, yaml_file_list):
        pb = PlaybookExecutor(
            playbooks=yaml_file_list,
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            passwords = None,
            options=self.options
        )
        result = pb.run()
        print (result)


if __name__ == "__main__":
    ansible_api = Ansible_api(["./hosts"])
#    ansible_api.run_adhoc("test01", "ping")
    ansible_api.run_adhoc("test01", "shell", "cat /etc/redhat-release")
#    ansible_api.run_adhoc("test01", "copy", "src=/tmp/xx.yml dest=/tmp/xx.yml")
#    ansible_api.run_adhoc("test01", "command", "python /tmp/cmdb_agent/resource_cpu_io_mem.py")
