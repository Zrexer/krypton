import httpx
import re
import bs4
import json
from . import toutils

onversion = int(toutils.toUtils.__version__.replace(".", ""))

def getRespone():
    resp = httpx.get("https://github.com/Zrexer/krypton/tree/main/versions").text
    parser = bs4.BeautifulSoup(resp, "html.parser")

    data = parser.findAll("script")

    script_data = re.search(r'<script.*?>(.*?)</script>', str(data[92]), re.DOTALL)
    if script_data:
        lastone = json.loads(script_data.group(1))['payload']['tree']
        return lastone

def checkVersions():
    dbs = []
    for item in getRespone()['items']:
        dbs.append(int(item['name'].replace(".", "")))
    
    for version in dbs:
        if version > onversion:
            return False
        else:
            pass

    return True