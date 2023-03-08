# KDE Connect transfer_handler
# Transfers latest Steam screenshot to any device using KDE Connect
import subprocess

device_name = 'snusk'

def transfer(filename):
    # wake up kdeconnect
    subprocess.call(['kdeconnect-cli', '-l'])

    # SEND IT
    print("sending {0} thru kdeconnect-cli".format(filename))
    subprocess.call(['kdeconnect-cli', '--share', filename, '-n', device_name])

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