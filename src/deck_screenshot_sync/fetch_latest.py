import os
from deck_screenshot_sync import steamstuff,vdf

no_transfer = False
try:
    from deck_screenshot_sync import transfer_handler
except:
    print("no transfer script")
    no_transfer = True

# Set variables
steam_dir = steamstuff.get_steam_dir()
steam_id = steamstuff.get_steam_id()
user = steamstuff.get_account_id()

# open and parse the screenshots.vdf file
d = vdf.parse(open("{0}userdata/{1}/760/screenshots.vdf".format(steam_dir, user & 0xFFFFFFFF)))

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

# If transfer handler present, upload it
if not no_transfer:
    print("Attemping to transfer file...")
    transfer_handler.transfer("{0}/userdata/{1}/760/remote/{2}".format(steam_dir, user & 0xFFFFFFFF, filename))
    # transfer_handler.transfer(os.path.basename(filename))
