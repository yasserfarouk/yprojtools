#!/usr/bin/env python
"""Installs needed packages to get all other helper scripts runnable."""
import os
import subprocess
import sys
this_dir = os.path.dirname(os.path.abspath(__file__))
requirements_dev = []
with open(os.path.join(this_dir, 'requirements-dev.txt'), 'r') as reqfile:
    tmp = reqfile.readlines()

for l in tmp:
    if l.strip().startswith('#'):
        continue
    requirements_dev.append(l)

if len(requirements_dev) > 0:
    subprocess.call(['pip', 'install'] + requirements_dev)

project_root = os.path.abspath(os.path.join(this_dir, '..'))
subprocess.call(['pip', 'install', '--upgrade', 'setuptools'])
subprocess.call(['pip', 'install', '-e', project_root])