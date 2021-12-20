""" Process class used in main method to list running process
    It will show running process pid and user corrently running it and
    and using os.system to kill the pid
"""
import os

class Process(object):
    def __init__(self, user, pid):
        self.user = user
        self.pid = pid

    def show_process(self):
        print(f" Process run by:  {self.user}")
        print(f" Process PID : {self.pid} ")

    def kill_process(pid):
        os.system("kill -9 " + pid)
        print(f"Process Succsessfully Terminated! ")

