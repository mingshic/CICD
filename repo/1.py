from subprocess import Popen, PIPE, STDOUT
p = Popen('python test.py', stdout=PIPE, stderr=STDOUT, shell=True)
for l in p.stdout: print (l.strip().decode("utf8"))

