#-*- coding: utf-8 -*-


from ..ansible_api.api import Ansible_api

def Run_ansible(host, host_tempfile, mode_parameter):
    if host_tempfile and mode_parameter:
        mode_ = []
        parameter_ = []
        ansible_run = Ansible_api([host_tempfile])
        # print("333333333333333333333333333 %s" % mode_parameter)
        # print("333333333333333333333333333 %s" % mode_parameter.split("\n"))
        # print ("222222222222222222222222222 %s" % str(len(mode_parameter.split("\n"))))
        # print ("333333333333333333333333333 %s" % mode_parameter.split("\n"))
        for mode_para in mode_parameter.split("\n"):
            # print ("11111111111111111111111111 %s:" % mode_para)
            # if mode_para != "" and ":" in mode_para:
            try:
                mode = mode_para.split(":")[0]
                parameter = mode_para.split(":")[1:]
                print("10101010101001 %s" % mode)
                if len(parameter) >= 2:
                    print(1)
                    parameter = ":".join(parameter)
                else:
                    # print(parameter)
                    try:
                        print(3)
                        parameter = parameter[0]
                    except:
                        parameter = None
            except:
                print(4)
                mode = mode_para.split("：")[0]
                parameter = mode_para.split("：")[1:]
                if len(parameter) >= 2:
                    parameter = ":".join(parameter)
                else:
                    print("5555555555555555555555555555555 %s" % parameter)
                    try:
                        parameter = parameter[0]
                    except:
                        parameter = None
            # print (host,mode,parameter)
            try:

                print(host, mode, parameter)
                ansible_run.run_adhoc(host, mode, parameter)
            except:
                pass
            mode_.append(mode)
            parameter_.append(parameter)
        return mode_, parameter_