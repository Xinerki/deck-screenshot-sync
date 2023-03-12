# deck-screenshot-sync
auto-upload screenshots made from the deck onto your pc or phone or idk!!
## _As seen on [reddit](https://www.reddit.com/r/SteamDeck/comments/11kqc95/i_made_a_script_to_auto_upload_steam_screenshots/)!!_

## WIP
the script is as WIP as this readme

![under construction!!!](http://motions.cat/gif/koujichu256.gif)

## Screenshot Sync Methods

Configuration is stored within `~/.config/autoscreenshot.config`:

| key                     | possible values | description                                           |
|-------------------------|-----------------|-------------------------------------------------------|
| transfer-mode           | kde,local       | Set the transfer mode type/service for autoscreenshot |
| kde-connect-device-name | <string>        | Set the device name when using KDE connect.           |
| local-target            | <string>        | Set the destination folder when using local mode.     |

### KDE Connect

Installing KDE connect
```
flatpak remote-add --if-not-exists kdeapps --from https://distribute.kde.org/kdeapps.flatpakrepo
sudo flatpak install org.kde.kdeconnect
``

Before EVERYTHING make sure you have kdeconnect all configured and your deck is paired 
with the device you want to send things to (also probably configure the folder you want 
stuff to go to too), I might write a guide for that eventually but yea...


### KDE Connect Configuration via GUI

Next, you'll have to edit your `~/.config/autoscreenshot.config` configuration file to have the 
name of your linked device, to do that:

- open your favorite terminal
- type `kdeconnect-cli -l`
- you will probably recognize the device you want to use, then copy its name
- open `transfer_handler.py` in your favorite (text) editor
- replace the 'snusk' in `device_name = 'snusk'` with the name of your linked device
- save and ur done!! move on to installation

### KDE Connect Configruation via CLI

Reference https://helpmanual.io/help/kdeconnect-cli/ to setup KDE connect without a desktop/desktop mode. This 
CLI version doesn't seem to be available in the KDEConnect flatpak. The Pacman package `kdeconnect` will work, 
but such packages installed by the user may be overwritten on system updates.

```
$ kdeconnect-cli -l
- Pixel 7: <LONG_ID> (paired and reachable)
1 device found
```

Edit your configuration:
```
{
	"transfer-mode": "kde-connect",
	"local-target": "",
	"kde-connect-device-name": "Pixel 7"
}

```

## Installation

Requires Python3, which should already be the default on the Steam Deck.

### PyPi installation (coming soon?)

### Installation from GitHub

Note: Add '-v' to `pip3` below to see setup installation messages + debug information.
```
git clone https://github.com/Xinerki/deck-screenshot-sync.git autoscreenshot
cd autoscreenshot
pip3 install .
```

If you want to test the install with pipenv, you can use:
```
pipenv install .
```

```
