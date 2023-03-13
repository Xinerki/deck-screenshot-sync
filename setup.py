#!/usr/bin/env python
import os
import shutil
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install as _install

file_dir = os.path.dirname(os.path.realpath(__file__))

# Create post install method for arbitrary data files
# Not sure how to raise exceptions in setup.py like this (yet)
# For now, use a file
def _post_install(dir):
    result = subprocess.run(['python3', 'post-install.py'],
         cwd=f"{file_dir}/src/deck_screenshot_sync")
    print(f"Post install result: {result}")
    if result.returncode != 0:
        raise Exception(f"Post installation failed! {result}")

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install tasks...")

setup(
    name='deck-screenshot-sync',
    version='0.1.1',
    author='Xin (Xinerki)',
    url='https://github.com/Xinerki/deck-screenshot-sync',
    packages=find_packages('src', exclude=['test']),
    package_dir={"":"src"},
    download_url='http://pypi.python.org/pypi/deck-screenshot-sync',
    project_urls={
        'Source': 'https://github.com/Xinerki/deck-screenshot-sync',
        'Tracker': 'https://github.com/Xinerki/deck-screenshot-sync/issues',
    },
    data_files=[
        ('config', ['src/deck_screenshot_sync/configuration/autoscreenshot.config'])
    ],
    description='Auto-upload screenshots made from the deck onto your PC/Mobile device',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia',
    ],
    cmdclass={'install': install},
)

print("Post installation log: /tmp/autoscreenshot.log")
