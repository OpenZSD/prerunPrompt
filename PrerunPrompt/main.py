import sys
import argparse
import time
import re
import subprocess
from screeninfo import get_monitors
sys.path.append('..')

def getDim(resString):
    if(re.match(r'\A\d{1,}x\d{1,}\Z', resString)):
        values=re.findall(r'\d+', resString)
        return (int(values[0]), int(values[1]))
    else:
        return None

def getScreenResolution():
    mon = get_monitors()[0]
    return (mon.width, mon.height)

def mainFunc():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", nargs=1, help="Command to run.", required=True)
    parser.add_argument("-m", nargs=1, help="Message to show", required=True)
    parser.add_argument("-s", nargs=1, help="Window size: 'fullscreen' or '#x#'", required=False, default=["fullscreen"])
    parser.add_argument("-t", type=int, nargs=1, help="Seconds to timeout", required=False, default=[0])
    args = parser.parse_args()

    res = None
    print(args.s[0].lower())
    if(args.s[0].lower() == "fullscreen"):
        res = getScreenResolution()
    else:
        res = getDim(args.s[0].lower())

    abortRun = True
    if(res):
        try:
            import PySimpleGUI as sg     
        except:
            print("Import error, make sure 'setupPrerunPrompt' is run.")
            sys.exit(1)
        innerCol=[[sg.B('START')]]
        midCol=[[sg.Text(args.m[0], justification='center')],[sg.Column(innerCol, vertical_alignment='center', justification='center')]]
        #outerCol=[[sg.Column(midCol, vertical_alignment='center', justification='center')]]
        win=sg.Window(title=" ", layout=[[sg.Column(midCol, vertical_alignment='center', justification='center',  k='-C-')]], size=res, margins=(100, 50))
        event, elements = win.read(timeout=args.t[0]*1000) if (args.t[0] > 0) else win.read() 

        if((event == "START") or ((event == "__TIMEOUT__"))):
            abortRun = False 
    else:
        print("Error, bad screen size")
        sys.exit(1)
    if(not abortRun):
        subprocess.Popen(args.c[0], shell=True)      

if __name__ == '__main__':
    mainFunc()
