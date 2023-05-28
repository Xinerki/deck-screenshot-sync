import os
import vdf
import steamstuff

no_transfer = False
try:
    import transfer_handler
except:
    print("no transfer script")
    no_transfer = True

steamdir = steamstuff.steamdir

user = steamstuff.GetAccountId()

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
