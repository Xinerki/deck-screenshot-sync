# KDE Connect transfer_handler
# Transfers latest Steam screenshot to any device using KDE Connect
import subprocess

device_name = 'snusk'

def transfer(filename):
    print("sending {0} thru kdeconnect-cli".format(filename))
    subprocess.call(['kdeconnect-cli', '--share', filename, '-n', device_name])