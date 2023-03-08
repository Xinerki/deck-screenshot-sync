# deck-screenshot-sync
auto-upload screenshots made from the deck onto your pc or phone or idk!!

# WIP
the script is as WIP as this readme

# Installation
barebones guide
```bash
chmod +x receive.sh
cp autoscreenshot.service ~/.config/systemd/user/autoscreenshot.service
cp autoscreenshot.path ~/.config/systemd/user/autoscreenshot.path
systemctl --user daemon-reload
kdeconnect-cli -l
systemctl --user enable --now autoscreenshot.path
```