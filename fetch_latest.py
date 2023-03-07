import os
import shutil
import vdf
no_transfer = False
try:
    import transfer_handler
except:
    print("no transfer script")
    no_transfer = True

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

print("MostRecent: {0}".format(users[str(user)]['PersonaName']))
print("SteamID: {0}".format(user))
print("AccountID: {0}".format(user & 0xFFFFFFFF))

# curdir = os.getcwd()
# dir = "{0}userdata/{1}/760".format(steamdir, user & 0xFFFFFFFF)
# os.chdir(dir)

# open and parse the screenshots.vdf file
d = vdf.parse(open("{0}userdata/{1}/760/screenshots.vdf".format(steamdir, user & 0xFFFFFFFF)))

# damn you case inconsistency
if 'screenshots' in d:
    screenshots = d['screenshots']
elif 'Screenshots' in d:
    screenshots = d['Screenshots']

latest = 0

for game in screenshots:
    for screenshot in screenshots[game]:
        if 'creation' in screenshots[game][screenshot]:
            creation = int(screenshots[game][screenshot]['creation'])
            if creation > latest:
                latest = creation
                gameid = int(game)
                screenshotid = int(screenshot)
                filename = screenshots[game][screenshot]['filename']

print("latest screenshot:")
print("{0}: {1} {2}".format(latest, gameid, screenshotid))

# os.chdir(curdir)
# shutil.copy2("{0}/remote/{1}".format(dir, filename), os.path.basename(filename))

#if transfer handler present, upload it
if not no_transfer:
    transfer_handler.transfer("{0}/userdata/{1}/760/remote/{2}".format(steamdir, user & 0xFFFFFFFF, filename))
    # transfer_handler.transfer(os.path.basename(filename))
