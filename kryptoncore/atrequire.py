import sys
from . import interminal
from . import forgithub
import threading
import site
import os

reqconsole = interminal.inConsole()
kryversion = forgithub.checkVersions()
version = sys.version
allmodules = [
    "httpx",
    "prompt_toolkit",
    "bs4",
    "flask"
]

def getAllModules():
    sites = site.getsitepackages()
    items = []
    for package in sites:
        for file in os.listdir(package):
            items.append(file)

    return items

def request():
    try:
        if not version[0] == "3":
            reqconsole.close_message()
            reqconsole.update_message("Your Python Version is Not Work for Krypton", "err")
            exit(1)
            
        if not kryversion:
            reqconsole.close_message()
            reqconsole.update_message("Your Krypton Version is out of Date, please Download it from Github: https://github.com/Zrexer", "err")
            exit(1)

        yall = getAllModules()

        for item in allmodules:
            if not item in yall:
                reqconsole.close_message()
                reqconsole.update_message("Please Download Moudle '{}'".format(item), "err")
                reqconsole.update_message("`pip install {}`\n".format(item))
                exit(1)
            else:pass

        reqconsole.close_message()
        print()

    except KeyboardInterrupt:
        reqconsole.close_message()
        exit(1)

def start():
    th1 = threading.Thread(target=reqconsole.animate_message, args=("[+] Checking Updates ...",))
    th2 = threading.Thread(target=request)

    th1.start()
    th2.start()

    th2.join()
    th1.join()