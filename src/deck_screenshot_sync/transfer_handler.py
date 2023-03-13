# KDE Connect transfer_handler
# Transfers latest Steam screenshot to any device using KDE Connect
import json
import pkg_resources
import os
import subprocess
import shutil
import sys

user_home = os.getenv("HOME")

def transfer(filename):

    # Read mode form user confi
    with open(f"{user_home}/.config/autoscreenshot.config", "r") as f:
        config = json.load(f)

    # Quick check...
    if not config.get('transfer-mode', ''):
        sys.exit(f"transfer-mode not set in {user_home}/.config/autoscreenshot.config! See README.md")

    # Handle config
    if config["transfer-mode"] == "kde-connect":
        if config.get('kde-connect-device-name', ''):
            device_name = config["kde-connect-device-name"]
        else:
            sys.exit(f"kde-connect-device-name not set in {user_home}/.config/autoscreenshot.config!")

        # wake up kdeconnect
        subprocess.call(['kdeconnect-cli', '-l'])

        # SEND IT
        print(f"sending {filanem} thru kdeconnect-cli")
        subprocess.call(['kdeconnect-cli', '--share', filename, '-n', device_name])

    elif config["transfer-mode"] == "local":
        # This mode is provided for file systems that have configured a
        # local path as a sync-target for something such as Google Photos / Dropbox
        if config.get('local-target', ''):
            local_dest = config["local-target"]
        else:
            sys.exit(f"local-target not set in {user_home}/.config/autoscreenshot.config!")

        dest_filename=os.path.basename(filename)
        dest_path=f"{local_dest}/{dest_filename}"
        print(f"sending {filename} thru local copy to {dest_path}")
        shutil.copy2(filename, dest_path)

"""

for the record: this is just one example of what you could do with this script
i just picked kdeconnect as it's a (surprisingly??) good way to quickly transfer a file
you could probably do a lot more with this, like automatically uploading to some image sharing service
something i did was send the screenshot thru a telegram bot using 'requests' library:

    import requests

    url = "https://api.telegram.org/bot"
    token = "u wish :)"
    chat_id = idk

    def transfer(filename):
        requests.post("{0}{1}/sendPhoto".format(url, token), data={'chat_id': chat_id}, files={'photo': open(filename, 'rb')})

"""
