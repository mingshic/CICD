# -*- coding:utf-8 -*-

import yaml, os
import subprocess
import hashlib
import time
import multiprocessing
import requests

from ..models import db, Ci_job_log


url = "http://192.168.52.143:5000/job"

def uuid_path_name():
    uuid = hashlib.md5()
    uuid.update(bytes(str(time.time()), encoding='utf-8'))
    file_id = uuid.hexdigest()
    return file_id


def write_log(data, log_directory):
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    with open(log_directory+"/"+"job.log", "a") as wp:
        wp.write(data+"\n")


def test_(filename, log_directory, source_directory):
    cases = {}
    origin_dir = os.getcwd()
    filename = os.path.join(filename).replace("\\","/")
    f = open(filename)
    yaml_load = yaml.load(f)
    os.chdir(source_directory)
    for key in yaml_load.keys():
        if key == "stages":
            for step in yaml_load[key]:
                for value in yaml_load.values():
                    if type(value) == dict and value["stage"] == step:
                        case = []
                        for command in value["script"]:
                            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                            print_info = ("$ " + command + "command_info_split_point" + p.stdout.read().decode("utf-8").strip())
                            write_log(print_info, log_directory)
                            case.append(["$ " + command, print_info])
                            cases.update({value["stage"]: case})
                    elif type(value) == list:
                        pass

    os.chdir(origin_dir)
    # ci_job_log = Ci_job_log(username=private_dir_name, log_path=log_directory, source=source)
    # # , stages=str(list(cases.keys())), content=str(list(cases.values())))
    # db.session.add(ci_job_log)
    # db.session.commit()
    # db.session.close()
    print (cases)
    return cases


def source_(item, source, private_dir_name, job_artifacts, job_artifacts_filename, log_directory, source_directory):
    if item == "1":
        if source.split("/")[-1][-4:] == ".git":
            private_dir = os.getcwd() + "/" + "jobs/runner" + "/" + private_dir_name
            log_dir = private_dir + "/" + "job_log"
            if not os.path.exists(private_dir):
                os.makedirs(private_dir)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)


            file_id = uuid_path_name()
            source_dir_uuid = private_dir + "/" + file_id

            source_dir = source.split("/")[-1][:-4]
            source_directory = source_dir_uuid + "/" + source_dir
            log_directory = log_dir + "/" + file_id

            if not os.path.exists(source_directory):
                os.makedirs(source_directory)

            p = subprocess.Popen("cd %s && git clone %s" % (source_dir_uuid, source), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            write_log(p.stdout.read().decode("utf-8").strip(), log_directory)


            job_artifacts_filename = source_directory + "/" + "%s_%s.yml" % (private_dir_name, file_id)
            with open(job_artifacts_filename, "w") as wp:
                wp.write(job_artifacts)

            ci_job_log = Ci_job_log(username=private_dir_name, log_path=log_directory, source=source)
            db.session.add(ci_job_log)
            db.session.commit()
            db.session.close()
            return (private_dir_name, job_artifacts_filename, log_directory, source_directory)



    elif item == "2":
        p1 = multiprocessing.Process(target=test_, args=(job_artifacts_filename,log_directory,source_directory,))
        # p2 = multiprocessing.Process(target=requests.post, args=(url, log_directory,))
        p1.start()
        p1.join()
        # p2.start()
        # p2.join()
        # test_(job_artifacts_filename, log_directory, source_directory)

