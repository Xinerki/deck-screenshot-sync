
import steamstuff

with open("autoscreenshot.path", 'w') as f:
    f.writelines("""
[Path]
PathModified=%h/.local/share/Steam/userdata/{}/760/screenshots.vdf
Unit=autoscreenshot.service
    """.format(steamstuff.GetAccountId()))

print("Successfully generated autoscreenshot.path (probably)")