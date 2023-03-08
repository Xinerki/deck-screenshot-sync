import os
import vdf

isDeck = True

if isDeck:
    steamdir = os.getenv("HOME") + "/.local/share/Steam/"
else:
    steamdir = "C:/Program Files (x86)/Steam/"

# get the current steam user's SteamID
def GetSteamId():
    d = vdf.parse(open("{0}config/loginusers.vdf".format(steamdir), encoding="utf-8"))
    users = d['users']
    for id64 in users:
        if users[id64]["MostRecent"] == "1":
            user = int(id64)
            print("MostRecent: {0}".format(users[str(user)]['PersonaName']))
            print("SteamID: {0}".format(user))
            print("AccountID: {0}".format(user & 0xFFFFFFFF))
            return user
        
# get the current steam user's AccountID
def GetAccountId():
    return GetSteamId() & 0xFFFFFFFF