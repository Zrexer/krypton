from .interminal import inConsole, TerminalColors
from .xssparser import XssParser
from .childprocess import ChildProcess
from .hashclip import HashClip
from .basefamily import BaseFamily
from .xssparser import XssParser
from .otherhost import lunchMain
from prompt_toolkit import prompt
from typing import Callable
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
import prompt_toolkit.lexers
import re

console = inConsole()
child = ChildProcess()
base = BaseFamily()
hashclip = HashClip()
xss = XssParser()
color = TerminalColors()
stringCommands: dict = {}

class KryptonPromptLexer(prompt_toolkit.lexers.Lexer):
    def __init__(self, regex_mapping):
        super().__init__()
        self.regex_mapping = regex_mapping

    def lex_document(self, document: Document) -> Callable[[int], StyleAndTextTuples]:
        def lex(_: int):
            line = document.text
            tokens = []
            while len(line) != 0:
                for pattern, style_string in self.regex_mapping.items():
                    match: re.Match = pattern.search(line)

                    if not match:
                        continue
                    else:
                        pass
                    match_string = line[:match.span()[1]]
                    line = line[match.span()[1]:]
                    tokens.append((style_string, match_string))
                    break
            return tokens
        return lex

class BufferList(object):
    def __init__(self,
                 List: list = [],
                 ):
        
        self.list = List
        
    def parse(self):
        bfd = {}

        for i in range(len(self.list)):
            bfd["_"+str(i+1)] = self.list[i]

        return bfd

    def isexists(self, target):
        if target in self.list:
            return True
        else:return False

    def isinfrontof(self, target, indexes):
        isit = False

        if target in self.list:
            try:
                indx = self.list.index(target)
                if indx == indexes:
                    isit = True
                else:isit = False
            except Exception as e:return e
        
        return isit
    
    def indexexists(self, target):
        if target in self.list:
            return self.list.index(target)
        else:return False

class BufferString(object):
    def __init__(self,
                 listed_data = [],
                 __help: str = "",
                 __discription: str = ""
                 ):

        self.listed_data = listed_data
        self.forHelp = __help
        self.dis = __discription
        self.status_help = True
        self.status_dis = True
        self.pyVersion = "3"
        self.data = []
    
    def __setcommands__(self, __key, __value):
        stringCommands[__key] = __value
        return stringCommands
    
    def getDictArgv(self):
        return BufferList(self.listed_data).parse()
    
    def addFlag(self, *flags, mode: str = "in_front_of"):
        flg = list(flags)
        for i in range(len(flg)):
            self.__setcommands__(str(i+1), flg[i])

        if mode == "in_front_of":
            for key, val in BufferString(self.listed_data).getDictArgv().items():

                if str(val) in flg:
                    keyx = int(str(key).replace("_", ""))
                    keyx += 1
                    if not f"_{keyx}" in BufferString(self.listed_data).getDictArgv().keys():
                        self.data.append("Null")
                        pass
                    else:
                        self.data.append(BufferString(self.listed_data).getDictArgv()[f"_{keyx}"])
                        pass
                
                else:
                    pass
            return self.data

class Compileds(object):
    numbers = re.compile(r"^\d+(\.\d+)?")
    text = re.compile(r"^.")
    StringMode1 = re.compile(r'^\"([^"]*)\"')
    StringMode2 = re.compile(r"^'([^']*)'")
    Something1 = re.compile(r'^-[a-zA-Z_]*')
    Something2 = re.compile(r"^[a-zA-Z]+\.")
    Something3 = re.compile(r"^\$")
    xsswork = re.compile(r"^@xss")
    locate = re.compile(r"@locate")
    hashable = re.compile(r"@hash")
    base = re.compile(r"@base")
    needhelp = re.compile(r"help")
    inpath = re.compile(r"^\.")
    backpath = re.compile(r"^\.\.")
    # Thanks to https://linuxcommandlibrary.com/
    # For Linux Commands
    oncommands = re.compile(r"^(cd|mv|cp|pwd|rm|rmdir|sudo|grep|head|mount|curl|ps|echo|if|man|dd|cut|dig|time|sleep|getconf|telnet|cat|uname|neofetch|top|lspci|lsblk|uptime|df|cal|uppower|ifconfig|ipconfig|nmap|sqlmap|hydra|krypton|awk|hciconfig|service|touch|ln|ls|umount|chmod|del|du|watch|tmux|vim|nano|emacs|mkdir|dir|gio|trash-empty|gvfs-trash|chown|chgrp|xclip|xdotool|ydotool|wtype|cancel|enable|disable|lpq|netcat|ping|lsof|find|fd|history|locate|wich|where|whereis|git|ssh|ffmpeg|play|apt|snap|flatpak|yum|dnf|pkg|apt-get|pacman|pip|npm|gem|zypper|dpkg|apt-cache|fi)")
    exitable = re.compile(r"^(exit|shutdown|poweroff|reboot)")

RegexMap = {
    Compileds.oncommands: "#d1de21",
    Compileds.StringMode1: "#0aa31e",
    Compileds.StringMode2: "#0aa31e",
    Compileds.Something1: "#9718ba",
    Compileds.Something2: "#1917bd",
    Compileds.Something3: "#1917bd",
    Compileds.xsswork: "#2cb8b3",
    Compileds.locate: "#2cb8b3",
    Compileds.hashable: "#2cb8b3",
    Compileds.base: "#2cb8b3",
    Compileds.needhelp: "#0acc34",
    Compileds.exitable: "#e80c0c",
    Compileds.numbers: "#ffa500",
    Compileds.text: "#ffffff"
}

def KryptonCommandLine():
    while 1:
        try:
            print("\n\r" + color.WHITE + "[" + color.GREEN + child.subester() + color.WHITE + "]~[" + color.RED + "KRY" + color.WHITE + "]")
            fprompt = prompt("$ ", lexer=KryptonPromptLexer(RegexMap))
            if fprompt.startswith("cd"):
                goto = fprompt[3:]
                status = child.changeway(goto)

                if not status:
                    console.update_message("KRY@REDPath Does not exist or Path is not DIR", "err")
            
            elif fprompt.startswith("@xss"):
                if fprompt[5:].isdigit():
                    for _ in range(int(fprompt[5:])):
                        print(xss.randomSelect())
                else:
                    print(xss.randomSelect())

            elif fprompt.startswith("@locate"):
                lunchMain()

            elif fprompt.startswith("@hash"):
                algorithm = BufferString(fprompt.split()).addFlag("--mode")
                makeit = BufferString(fprompt.split()).addFlag("--make")
                if len(makeit) >= 1:
                    data = fprompt[fprompt.index("--make")+7:] if not makeit[0] in ("Null", "--make", "--mode") else ""
                    if len(algorithm) >= 1:
                        if algorithm[0] in (
                            "md5",
                            "sha1",
                            "sha224",
                            "sha256",
                            "sha384",
                            "sha512"
                        ):
                            if algorithm[0] == "md5": console.update_message(hashclip.md5(data))
                            elif algorithm[0] == "sha1": console.update_message(hashclip.sha1(data))
                            elif algorithm[0] == "sha224": console.update_message(hashclip.sha224(data))
                            elif algorithm[0] == "sha256": console.update_message(hashclip.sha256(data))
                            elif algorithm[0] == "sha384": console.update_message(hashclip.sha384(data))
                            elif algorithm[0] == "sha512": console.update_message(hashclip.sha512(data))
                        else:
                            console.update_message(hashclip.md5(data))

            elif fprompt.startswith("@base"):
                algorithm = BufferString(fprompt.split()).addFlag("--mode")
                slide = BufferString(fprompt.split()).addFlag("--slide")
                makeit = BufferString(fprompt.split()).addFlag("--make")
                if len(makeit) >= 1:
                    data = fprompt[fprompt.index("--make")+7:] if not makeit[0] in ("Null", "--make", "--mode") else ""
                    if len(slide) >= 1:
                        if slide[0] in ("enc", "dec"):
                            if len(algorithm) >= 1:
                                if algorithm[0] in (
                                    "base16",
                                    "base32",
                                    "base64",
                                    "base85"
                                ):
                                    if algorithm[0] == "base16": console.update_message(base.base16enc(data)) if slide[0] == "enc" else console.update_message(base.base16dec(data))
                                    elif algorithm[0] == "base32": console.update_message(base.base32enc(data)) if slide[0] == "enc" else console.update_message(base.base32dec(data))
                                    elif algorithm[0] == "base64": console.update_message(base.base64enc(data)) if slide[0] == "enc" else console.update_message(base.base64dec(data))
                                    elif algorithm[0] == "base85": console.update_message(base.base85enc(data)) if slide[0] == "enc" else console.update_message(base.base85dec(data))
                                else:
                                    console.update_message(base.base64enc(data)) if slide[0] == "enc" else console.update_message(base.base64dec(data))

            elif fprompt == "help":
                console.update_message("\nUsage of Krypton Client Side\n\n  @xss <NUMBER>: get a randomly xss source\n  @hash --mode <MODE> --make <YOUR SENTENCE>: make hash\n  @base --slide <enc OR dec> --mode <BASE FAMILY MODE> --make <YOUR SENTENCE>\n  @locate: run server on localhost in randomly port")

            elif fprompt in ("exit", "shutdown", "poweroff"):
                exit(1)
            
            else:
                child.execute(fprompt)

        except Exception as KRYPTON_ERROR:
            console.update_message("Error Detected: KRY@RED{}".format(str(KRYPTON_ERROR)))
            pass
