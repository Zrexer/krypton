import random
import os
from . import interminal

xssconsole = interminal.inConsole()
pathlike = os.path

if not pathlike.exists("xss.txt"):
    xssconsole.update_message(f"Path of KRY@YELLOWXSSKRY@WHITE does not exist, \nPlease download the Last Version of Krypton from GitHub", "err")
    exit(1)

class XssParser(object):
    def __init__(self) -> None:
        pass

    allPayloads = open("./xss.txt", 'r').read()
    allCount = len(allPayloads.split("\n"))
    firstF = allPayloads.split("\n")[0:1001]
    secF = allPayloads.split("\n")[1002:2001]
    threeF = allPayloads.split("\n")[2002:3001]
    fourF = allPayloads.split("\n")[3002:4001]
    fiveF = allPayloads.split("\n")[4002:5001]
    sixF = allPayloads.split("\n")[5002:6001]
    sevenF = allPayloads.split("\n")[6002:7001]
    eightF = allPayloads.split("\n")[7002:-1]
    
    
    def randomSelect(self):
        which = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        
        if which == 1:return random.choice(XssParser.firstF)
        elif which == 2:return random.choice(XssParser.secF)
        elif which == 3:return random.choice(XssParser.threeF)
        elif which == 4:return random.choice(XssParser.fourF)
        elif which == 5:return random.choice(XssParser.fiveF)
        elif which == 6:return random.choice(XssParser.sixF)
        elif which == 7:return random.choice(XssParser.sevenF)
        elif which == 8:return random.choice(XssParser.eightF )