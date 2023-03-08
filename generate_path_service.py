
import os
import vdf

isDeck = True

if isDeck:
    steamdir = os.getenv("HOME") + "/.local/share/Steam/"
else:
    steamdir = "C:/Program Files (x86)/Steam/"

# get the current steam user's AccountID
d = vdf.parse(open("{0}config/loginusers.vdf".format(steamdir), encoding="utf-8"))
users = d['users']
for id64 in users:
    if users[id64]["MostRecent"] == "1":
        user = int(id64)

with open("autoscreenshot.path", 'w') as f:
    f.writelines("""
[Path]
PathModified=%h/.local/share/Steam/userdata/{}/760/screenshots.vdf
Unit=autoscreenshot.service
    """.format(user & 0xFFFFFFFF))