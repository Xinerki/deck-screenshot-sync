import platform
import os
import sys

from deck_screenshot_sync import vdf

# 'Linux', 'Darwin', 'Java', 'Windows'
operating_system = platform.system()

def get_steam_dir():
    if operating_system == ("Linux" or "Darwin"):
        steam_dir = os.getenv("HOME") + "/.local/share/Steam/"
    elif operating_system == "Windows":
        steam_dir = "C:/Program Files (x86)/Steam/"
    else:
        sys.exit(f"Cannot handle operating system: {operating_system}")

    return steam_dir

# get the current steam user's SteamID
def get_steam_id():
    steam_dir = get_steam_dir()
    d = vdf.parse(open("{0}config/loginusers.vdf".format(steam_dir), encoding="utf-8"))
    users = d['users']
    for id64 in users:
        if users[id64]["MostRecent"] == "1":
            user = int(id64)
            print("MostRecent: {0}".format(users[str(user)]['PersonaName']))
            print("SteamID: {0}".format(user))
            print("AccountID: {0}".format(user & 0xFFFFFFFF))
            return user
        
# get the current steam user's AccountID
def get_account_id():
    return get_steam_id() & 0xFFFFFFFF
