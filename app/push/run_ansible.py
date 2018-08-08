#-*- coding: utf-8 -*-


# from ..ansible_api.api import Ansible_api
import yaml,os
import hashlib,time
import subprocess

def uuid_path_name():
    uuid = hashlib.md5()
    uuid.update(bytes(str(time.time()), encoding='utf-8'))
    file_id = uuid.hexdigest()
    return file_id

def write_yaml(host, host_tempfile, mode_parameter, user):
    origin_dir = os.getcwd()
    touch_comdir = origin_dir + "/" + "app/push/touch_command" + "/" + user
    touch_py = touch_comdir + "/" + "pys"
    touch_yml = touch_comdir + "/" + "ymls"
    uuid_dir = uuid_path_name()
    if not os.path.exists(touch_comdir):
        os.makedirs(touch_comdir)
    if not os.path.exists(touch_py):
        os.makedirs(touch_py)
    if not os.path.exists(touch_yml):
        os.makedirs(touch_yml)
    touch_yml_file = user + "_" + uuid_dir + ".yml"
    touch_py_file = user + "_" + uuid_dir + ".py"

    touch_file_py = touch_py + "/" + touch_py_file
    touch_file_yml = touch_yml + "/" + touch_yml_file


    with open(touch_file_yml, "w") as wp:
        wp.write(mode_parameter)
    return origin_dir, host, host_tempfile, touch_file_yml, touch_file_py

def load_yaml(host, host_tempfile, mode_parameter, user):
    origin_dir, host, host_tempfile, touch_file_yml, touch_file_py = write_yaml(host, host_tempfile, mode_parameter, user)
    filename = os.path.join(touch_file_yml).replace("\\", "/")
    f = open(filename)
    yaml_load = yaml.load(f)
    return yaml_load, host, host_tempfile, origin_dir, touch_file_py,


def write_py(yaml_loaded, host, host_tempfile, origin_dir, touch_file_py):
    mode_ = []
    parameter_ = []
    tasks = yaml_loaded["tasks"]
    fwrite = open(touch_file_py, "a")
    fwrite.write("#-*- coding: utf-8 -*-\n")
    fwrite.write("import os,sys\n")
    fwrite.write("sys.path.append('%s')\n" % origin_dir)
    fwrite.write("from app.ansible_api.api import Ansible_api\n")
    fwrite.write("ansible_api = Ansible_api(['%s'])\n" % host_tempfile)
    for task in tasks:
        task = list(task.items())[0]
        fwrite.write("ansible_api.run_adhoc('%s', '%s', '%s')\n" % (host, task[0], task[1]))
        mode_.append(task[0])
        parameter_.append(task[1])
    fwrite.close()
    return mode_, parameter_



def yaml_to_py(host, host_tempfile, mode_parameter, user):
    yaml_loaded, host, host_tempfile, origin_dir, touch_file_py = load_yaml(host, host_tempfile, mode_parameter, user)
    mode_, parameter_ = write_py(yaml_loaded, host, host_tempfile, origin_dir, touch_file_py)
    return touch_file_py, mode_, parameter_

def Run_ansible(host, host_tempfile, mode_parameter, user):
    py_file, mode_, parameter_ = yaml_to_py(host, host_tempfile, mode_parameter, user)
    p = subprocess.Popen("python %s" % py_file, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print (p.stdout.read().decode("utf-8").strip())
    return mode_, parameter_

    # if host_tempfile and mode_parameter:
    #     mode_ = []
    #     parameter_ = []
    #     ansible_run = Ansible_api([host_tempfile])
    #     # print("333333333333333333333333333 %s" % mode_parameter)
    #     # print("333333333333333333333333333 %s" % mode_parameter.split("\n"))
    #     # print ("222222222222222222222222222 %s" % str(len(mode_parameter.split("\n"))))
    #     # print ("333333333333333333333333333 %s" % mode_parameter.split("\n"))
    #     for mode_para in mode_parameter.split("\n"):
    #         # print ("11111111111111111111111111 %s:" % mode_para)
    #         # if mode_para != "" and ":" in mode_para:
    #         try:
    #             mode = mode_para.split(":")[0]
    #             parameter = mode_para.split(":")[1:]
    #             print("10101010101001 %s" % mode)
    #             if len(parameter) >= 2:
    #                 print(1)
    #                 parameter = ":".join(parameter)
    #             else:
    #                 # print(parameter)
    #                 try:
    #                     print(3)
    #                     parameter = parameter[0]
    #                 except:
    #                     parameter = None
    #         except:
    #             print(4)
    #             mode = mode_para.split("：")[0]
    #             parameter = mode_para.split("：")[1:]
    #             if len(parameter) >= 2:
    #                 parameter = ":".join(parameter)
    #             else:
    #                 print("5555555555555555555555555555555 %s" % parameter)
    #                 try:
    #                     parameter = parameter[0]
    #                 except:
    #                     parameter = None
    #         # print (host,mode,parameter)
    #         try:
    #
    #             print(host, mode, parameter)
    #             ansible_run.run_adhoc(host, mode, parameter)
    #         except:
    #             pass
    #         mode_.append(mode)
    #         parameter_.append(parameter)
    #     return mode_, parameter_