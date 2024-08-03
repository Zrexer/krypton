import os
import subprocess
from . import onplatform

childplatform = onplatform.onPlatform()
pathlike = os.path

class ChildProcess(object):
    def __init__(self) -> None:
        self.onpath = os.getcwd()

    def execute(self,
                command: str = "",
                capture_output: bool = False):
        
        if not capture_output:
            os.system(command)
        else:
            return subprocess.getoutput(command)
        
    def subester(self):
        if self.pwd.startswith(self.onpath):
            return self.pwd.replace(self.onpath, "~")
        else:
            return self.pwd
        
    def changeway(self, path: str):
        if not pathlike.exists(path):
            return False
        
        elif not pathlike.isdir(path):
            return False
        
        else:
            os.chdir(path)
            return True
    
    @property
    def pwd(self):
        return os.getcwd()