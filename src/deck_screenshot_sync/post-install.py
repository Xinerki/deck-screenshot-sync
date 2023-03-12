#!/usr/bin/env python
import os
import logging
import shutil
import subprocess

# Log actions
logging.basicConfig(
    filename="/tmp/autoscreenshot.log", 
    filemode='w',
    level=logging.DEBUG
)
logger = logging.getLogger()
logging.info("Running post installation tasks...")

logger.debug("Setting variables")
user_home = os.getenv("HOME")
file_dir = os.path.dirname(os.path.realpath(__file__))
config_src_path = f"{file_dir}/configuration"

# Generate path service unit
logger.debug("Generating systemd unit...")
try:
    result = subprocess.run(['python', f"{file_dir}/generate_path_service.py"],
         cwd=os.path.join(file_dir))
    logger.debug(result)
except Exception as e:
    raise Exception(e)

# Install systemd unit files
try:
    logger.debug(f"Copying service files to {user_home}/.config/systemd/user")
    files = [
        "autoscreenshot.path",
        "autoscreenshot.service"
    ]

    # systemd stuff...
    for f in files:
        file_src = f"{config_src_path}/{f}"
        file_dest = f"{user_home}/.config/systemd/user/{f}"
        shutil.copyfile(file_src, file_dest)

    # copy in config
    file_src = f"{config_src_path}/autoscreenshot.config"
    file_dest = f"{user_home}/.config/autoscreenshot.config"
    # Only overwrite the user dest if it doesn't exist
    if os.path.isfile(file_dest):
        logger.warning(f"Destination config {file_dest} exists, skipping. Remove this file to reset")
    else:
        shutil.copyfile(file_src, file_dest)

except Exception as e:
    raise Exception(e)

# Reload user systemd
try:
    logger.debug("Reloading user systemd...")
    result = subprocess.run(['systemctl', '--user', 'daemon-reload'],
         cwd=os.path.join(file_dir), capture_output=True, encoding="UTF-8" )
    logger.debug(str(result).replace('\\n', '\n'))
    if result.returncode != 0:
        raise Exception(result)

    logger.debug("Enabling autoscreenshot service...")
    result = subprocess.run(['systemctl', '--user', 'enable', '--now', 'autoscreenshot.path'],
         cwd=os.path.join(file_dir), capture_output=True, encoding="UTF-8" )
    logger.debug(str(result).replace('\\n', '\n'))
    if result.returncode != 0:
        raise Exception(result)

except Exception as e:
    raise Exception(e)

try:
    logger.debug("Checking service status...")
    result = subprocess.run(['systemctl', '--user', 'status', 'autoscreenshot.path'],
         cwd=os.path.join(file_dir), capture_output=True, encoding="UTF-8" )
    logger.debug(str(result).replace('\\n', '\n'))

    if result.returncode != 0:
        raise Exception(result)
except Exception as e:
    raise Exception(e)

logger.debug("Done!")
