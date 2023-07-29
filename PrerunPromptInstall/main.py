import os
import subprocess
import sys
from os import path
sys.path.append('..')
import PrerunPromptInstall

def mainFunc():
    shellFile = str(os.path.dirname(os.path.abspath(PrerunPromptInstall.__file__)))+"/setup/installDep.sh"
    subprocess.Popen("sudo chmod 555 "+shellFile, shell=True).wait()
    subprocess.Popen(shellFile, shell=True).wait()
if __name__ == '__main__':
    mainFunc()
