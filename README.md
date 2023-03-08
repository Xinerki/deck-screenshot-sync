# deck-screenshot-sync
auto-upload screenshots made from the deck onto your pc or phone or idk!!

# WIP
the script is as WIP as this readme

![under construction!!!](http://motions.cat/gif/koujichu256.gif)

# KDE Connect preparation
before EVERYTHING make sure you have kdeconnect all configured and your deck is paired with the device you want to send things to (also probably configure the folder you want stuff to go to too), i might write a guide for that eventually but ya

next you'll have to edit the `transfer_handler.py` script to have the name of your linked device, to do that:
- open your favorite terminal
- type `kdeconnect-cli -l`
- you will probably recognize the device you want to use, then copy its name
- open `transfer_handler.py` in your favorite (text) editor
- replace the 'snusk' in `device_name = 'snusk'` with the name of your linked device
- save and ur done!! move on to installation
# Installation

- TODO: does deck come with python3? or git??
- open youR terminal of choice
- do `git clone https://github.com/Xinerki/deck-screenshot-sync.git autoscreenshot` to clone the repo (autoscreenshot name is important!!)
- `cd autoscreenshot` to go into the folder
- do `chmod +x install.sh` then `./install.sh` and it should do everything for u!!

## TL;DR
```bash
git clone https://github.com/Xinerki/deck-screenshot-sync.git autoscreenshot
cd autoscreenshot
chmod +x install.sh
./install.sh
```