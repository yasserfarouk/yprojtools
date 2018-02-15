#!/usr/bin/env python
"""Pumps the version number in setup.py by 1 if possible."""
import datetime
import os

this_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(this_path, '..'))
with open(os.path.join(project_root, 'setup.py'), 'r') as file_name:
    lines = file_name.readlines()
name = None
current_version = None
short_description = ''
for i, l in enumerate(lines):
    l2 = l.replace(' ', '')
    if 'version=' in l2:
        location = l.find('version')
        before = l[:location]
        current_version = l.replace(' ', '').replace("'", '').replace(',', '')\
            .split('=')[-1].replace(' ', '') \
            .replace('\n', '')
    if 'description=' in l2:
        location = l.find('description')
        before = l[:location]
        short_description = l.replace(' ', '').replace("'", '')\
            .replace(',', '').split('=')[-1].replace(' ', '') \
            .replace('\n', '')
    if 'name=' in l2:
        location = l.find('name')
        before = l[:location]
        name = l.replace(' ', '').replace("'", '').replace(',', '')\
            .split('=')[-1].replace(' ', '') \
            .replace('\n', '')

if len(short_description) == 0:
    short_description = 'Package ' + name

if name is None:
    print('Could not find the package name in setup.py')
    exit(-1)
if current_version is None:
    print('Could not find version in setup.py')
    exit(-2)
package_path = os.path.join(project_root, name)
if not os.path.exists(package_path) or not os.path.isdir(package_path):
    print('Could not find package {} at {}'.format(name, project_root))
    exit(-3)
doc_path = os.path.join(project_root, 'docs')


def _update_template(conf_txt):
    conf_txt = conf_txt.replace('<<short_description>>', short_description)
    conf_txt = conf_txt.replace('<<package_name>>', name)
    conf_txt = conf_txt.replace('<<version>>', current_version)
    conf_txt = conf_txt.replace('<<year>>', str(datetime.datetime.now().year))
    conf_txt = conf_txt.replace('<<now>>', str(datetime.datetime.now()))
    return conf_txt


os.makedirs(doc_path, exist_ok=True)
conf_txt = None
doc_helpers_dir = os.path.join(this_path, 'doc_helpers')
for file_name in list(os.listdir(doc_helpers_dir)):
    if file_name.startswith('.'):
        continue
    path = os.path.join(doc_helpers_dir, file_name)
    if os.path.isdir(path):
        os.makedirs(os.path.join(doc_path, file_name), exist_ok=True)
    else:
        with open(path, 'r') as file:
            conf_txt = file.read()
        conf_txt = _update_template(conf_txt)
        with open(os.path.join(doc_path, file_name), 'w') as file:
            file.write(conf_txt)
current_dir = os.getcwd()
os.chdir(doc_path)
os.system('sphinx-apidoc -a -f -o . ../{}'.format(name))
os.system('make html')
os.chdir(current_dir)
