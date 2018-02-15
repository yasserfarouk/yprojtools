#!/usr/bin/env python
"""Prepares and uploads the project to pypi assuming that it uses Pipenv."""

import os
import subprocess
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(this_dir, '..'))

subprocess.check_output(['python', '{}/init_helpers.py'.format(this_dir)]
                        , stderr=subprocess.STDOUT)


pump_version = False
for arg in sys.argv[1:]:
    if arg in ('-f', '--force', '--pump-version'):
        pump_version = True



current_dir = os.getcwd()
os.chdir(this_dir)
subprocess.check_output(['python', '{}/convert_readme_to_rs.py'.format(
    this_dir)], stderr=subprocess.STDOUT)
if pump_version:
    subprocess.check_output(['python', '{}/pump_version_number.py'.format(
        this_dir)], stderr=subprocess.STDOUT)
subprocess.check_output(['python', '{}/update_doc.py'.format(this_dir)]
                        , stderr=subprocess.STDOUT)
subprocess.check_output(['python',
                         '{}/update_requirements_in_setup_from_pipenv.py'\
                         .format(this_dir)]
                        , stderr=subprocess.STDOUT)
os.chdir(project_root)
setup_txt = subprocess.check_output(['python', 'setup.py', 'sdist']
                                    , stderr=subprocess.STDOUT).decode()\
                                    .split('\n')
dist_file = None
for s in setup_txt:
    if s.startswith('removing'):
        dist_file = s.split("'")[1] + '.tar.gz'
if dist_file is None:
    print('Could not find dist file name in the output of setup.py sdist')
    sys.exit(-2)
print('Uploading {} to pypi'.format(dist_file))
subprocess.check_output(['twine', 'upload', 'dist/{}'.format(dist_file)])
os.chdir(current_dir)
