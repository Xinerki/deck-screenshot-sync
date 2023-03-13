
import os

from deck_screenshot_sync import steamstuff

file_dir = os.path.dirname(os.path.realpath(__file__))
configs=f"{file_dir}/configuration/autoscreenshot.path"

with open(configs, 'w') as f:
    f.writelines("""
[Path]
PathModified=%h/.local/share/Steam/userdata/{0}/760/screenshots.vdf
Unit=autoscreenshot.service
    """.format(steamstuff.get_account_id()))

print(f"Successfully generated {file_dir}/configuration/autoscreenshot.path")
