#!/bin/bash

# im not good at writing bash lmao ;w;

echo "Generating path service unit.."
python3 generate_path_service.py
echo "Copying service files.."
cp -v autoscreenshot.service ~/.config/systemd/user/autoscreenshot.service
cp -v autoscreenshot.path ~/.config/systemd/user/autoscreenshot.path
echo "Starting service.."
systemctl --user daemon-reload
systemctl --user enable --now autoscreenshot.path
echo "These angry messages are normal don't worry"
systemctl --user status autoscreenshot.path
echo "" # :v
echo "Does it say \"active (waiting)\"? awesome!!"