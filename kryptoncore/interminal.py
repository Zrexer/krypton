import time
import os

os.system("")

class TerminalColors(object):
    """Terminal Colors is an Object \n
    I Save them here to have a Better Control of them \n
    Actually Python Know them fields of `TerminalColors` object. \n
    You can use them in `update_message` function, from `inConsole` class, \n
    Just use the parameters Capitally. \n

    :params:
        @WHITE \n
        @GREEN \n
        @RED \n
        @YELLOW \n
        @Backwhite \n
        @Backgreen \n
        @Backyellow \n
        @BackBlue \n
        @Backpink \n
        @Backcyan \n
        @BackRed \n
        @green \n
        @red \n
        @blue \n
        @pink \n
        @yellow \n
        @darkblue \n
        @white \n
        @black \n
        @bold \n
        @underline \n
        @magenta \n
    """

    WHITE = "\001\033[0;38;5;231m\002"
    GREEN = "\001\033[0;38;5;46m\002"
    RED = "\001\033[0;38;5;196m\002"
    YELLOW = "\001\033[0;38;5;226m\002"

    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'

    green = '\033[32m'
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

class inConsole(object):
    """inConsole Class \n
    Made for print messages especially \n
    :params:
        @update_message
        @animate_message
        @close_message
    """
    def __init__(self) -> None:
        self.message_types = [
            'inf',
            'err',
            'warn'
        ]
        self.dbs = {'finish': False}
    
    def update_message(self,
                       message: str = "",
                       message_type: str = "inf"):
        
        """update_message Function \n
        This function print messages especially for Krypton, \n
        also you can add colors like this: \n

        ```
        console = inConsole()
        console.update_message("KRY@WHITE Hello KRY@YELLOW world KRY@WHITE")
        ```
        \nFor Colors you can read the Topic of `TerminalColors` Class
        """
        
        func_date = time.strftime("%y/%m/%d - %H:%M:%S")

        colored_message = message.replace("KRY@WHITE", TerminalColors.WHITE).replace("KRY@GREEN", TerminalColors.green) \
                                          .replace("KRY@RED", TerminalColors.red).replace("KRY@BLUE", TerminalColors.blue) \
                                          .replace("KRY@PINK", TerminalColors.pink).replace("KRY@YELLOW", TerminalColors.yellow) \
                                          .replace("KRY@DARKBLUE", TerminalColors.darkblue).replace("KRY@BLACK", TerminalColors.black) \
                                          .replace("KRY@UNDERLINE", TerminalColors.underline).replace("KRY@BOLD", TerminalColors.bold) \
                                          .replace("KRY@MAGENTA", TerminalColors.magenta).replace("KRY@BACKWHITE", TerminalColors.Backwhite) \
                                          .replace("KRY@BACKGREEN", TerminalColors.Backgreen).replace("KRY@BACKRED", TerminalColors.BackRed) \
                                          .replace("KRY@BACKBLUE", TerminalColors.BackBlue).replace("KRY@BACKCYAN", TerminalColors.Backcyan) \
                                          .replace("KRY@BACKYELLOW", TerminalColors.Backyellow).replace("KRY@BACKPINK", TerminalColors.Backpink)

        if message_type in self.message_types:
            if message_type == "inf":
                print(f"\n\r{TerminalColors.WHITE}[{TerminalColors.YELLOW}{func_date}{TerminalColors.WHITE}]-[{TerminalColors.GREEN}KryptoInfo{TerminalColors.WHITE}] {colored_message}", end="", flush=True)
            elif message_type == "err":
                print(f"\n\r{TerminalColors.WHITE}[{TerminalColors.YELLOW}{func_date}{TerminalColors.WHITE}]-[{TerminalColors.RED}KryptoError{TerminalColors.WHITE}] {colored_message}", end="", flush=True)
            elif message_type == "warn":
                print(f"{TerminalColors.WHITE}[{TerminalColors.YELLOW}{func_date}{TerminalColors.WHITE}]-[{TerminalColors.white}{TerminalColors.BackRed}KryptoWarn{TerminalColors.WHITE}] {colored_message}")
        else:
            pass

    def animate_message(self,
                        message: str):
        """animate_message Function \n
        this function is going to create a animated loading message \n
        use loading in client file.\n
        :params:
            @message
        """
        while 1:
            party = ["/", "|", "\\", "-"]
            if not self.dbs['finish']:
                for item in party:
                    print(f"\r{message} {item}", end="", flush=True)
                    print("\r", end="", flush=True)
            else:
                break

        pass

    def close_message(self):
        """close_message Function \n
        `close_message` created for disable the `animate_message`. \n
        """

        self.dbs['finish'] = True