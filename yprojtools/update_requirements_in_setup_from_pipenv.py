#!/usr/bin/env python
"""
A script to insert requirements from pipfile to setup.py.

The script assumes that both Pipfile and setup.py are in the same folder which is '..'. This can be changed by passing
one argument with the location of setup.py file
"""
import sys
import os
if len(sys.argv) > 1:
    this_dir = sys.argv[1]
this_file = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(this_file, '..'))

requirements = []
test_requirements = []


def from_pipenv():
    if os.path.exists(os.path.join(project_root, 'Pipfile')):
        from pipenv.project import Project
        from pipenv.utils import convert_deps_to_pip
        pfile = Project(chdir=False).parsed_pipfile
        requirements = convert_deps_to_pip(pfile['packages'], r=False)
        test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)
        return requirements, test_requirements
    else:
        return [], []


def from_requirements_file():
    requirements = []
    test_requirements = []
    if os.path.exists(os.path.join(project_root, 'requirements.txt')):
        with open(os.path.join(project_root, 'requirements.txt'), 'r') as reqfile:
            requirements += reqfile.readlines()
    if os.path.exists(os.path.join(project_root, 'requirements-dev.txt')):
        with open(os.path.join(project_root, 'requirements-dev.txt'), 'r') as reqfile:
            test_requirements += reqfile.readlines()
    if os.path.exists(os.path.join(this_file, 'requirements-dev.txt')):
        with open(os.path.join(this_file, 'requirements-dev.txt'), 'r') as reqfile:
            test_requirements += reqfile.readlines()
    if os.path.exists(os.path.join(project_root, 'requirements_dev.txt')):
        with open(os.path.join(project_root, 'requirements_dev.txt'), 'r') as reqfile:
            test_requirements += reqfile.readlines()
    return requirements, test_requirements


# read requirements from both Pipfile and requirements.txt files (both
# runtime and development)
req, test_req = from_pipenv()
req2, test_req2 = from_requirements_file()
requirements = req
for item in req2:
    if item not in requirements:
        requirements.append(item)
test_requirements = test_req
for item in test_req2:
    if item not in test_requirements:
        test_requirements.append(item)

# update requirements file
with open(os.path.join(project_root, 'requirements.txt'), 'w') as reqfile:
    reqfile.writelines(requirements)
with open(os.path.join(project_root, 'requirements-dev.txt'), 'w') as reqfile:
    reqfile.writelines(test_requirements)

with open(os.path.join(project_root, 'setup.py'), 'r') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'install_requires' in l:
        location = l.find('install_requires')
        before = l[:location]
        lines[i] = before + 'install_requires={},\n'.format(requirements)
with open(os.path.join(project_root, 'setup.py'), 'w') as f:
    f.writelines(lines)
