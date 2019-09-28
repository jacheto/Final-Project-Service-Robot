#!/usr/bin/env python


from six.moves import urllib
import requests
import json
import time




import subprocess
import shlex
import sys
import signal
import psutil

def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
        print(parent)
    except psutil.NoSuchProcess:
        print("parent process not existing")
        return
    children = parent.children(recursive=True)
    print(children)
    for process in children:
        print("try to kill child: " + str(process))
        process.send_signal(sig)

class Roscore(object):
    """
    roscore wrapped into a subprocess.
    Singleton implementation prevents from creating more than one instance.
    """
    __initialized = False
    def __init__(self):
        if Roscore.__initialized:
            raise Exception("You can't create more than 1 instance of Roscore.")
        Roscore.__initialized = True
    def run(self, command_list):
        try:
            self.roscore_process = subprocess.Popen(command_list)
            self.roscore_pid = self.roscore_process.pid  # pid of the roscore process (which has child processes)
        except OSError as e:
            sys.stderr.write('roscore could not be run')
            raise e
    def terminate(self):
        print("try to kill child pids of roscore pid: " + str(self.roscore_pid))
        kill_child_processes(self.roscore_pid)
        self.roscore_process.terminate()
        self.roscore_process.wait()  # important to prevent from zombie process
        Roscore.__initialized = False






def post(chave, valor):
    address = "http://10.0.0.2:5010"
    valor_json = json.dumps({'valor': valor, 'timestamp':time.time()})
    requests.post(url = address + "/post_data?chave=" + chave, data=valor_json)

def get(chave, get_timestamp=False):
    address = "http://10.0.0.2:5010"
    valor_json = urllib.request.urlopen(address + '/get_data?chave=' + chave).read()
    if valor_json == "":
        return ""
    valor_dict = json.loads(valor_json)
    if get_timestamp:
        return valor_dict['timestamp']
    
    return valor_dict['valor']



roscore = Roscore()
command_list = ['roslaunch', 'roboserv_simulation', 'roboserv_real.launch']
roscore.run(command_list)
time.sleep(20)
roscore.terminate()