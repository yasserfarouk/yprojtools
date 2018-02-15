#!/usr/bin/env python
"""Converts README file from markdown to restructured text.

You can pass the location of the README file to be converted as first parameter
If not passed, it is assumed that the README file is in the parent directory

"""
import pypandoc
import os
import sys

# converts markdown to reStructured
loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
if len(sys.argv) > 1:
    loc = sys.argv[1]
    if loc.endswith('README'):
        loc = loc[:-len('README')]

z = pypandoc.convert(os.path.join(loc, 'README'), 'rst', format='markdown')
# writes converted file
with open(os.path.join(loc, 'README.rst'), 'w') as outfile:
    outfile.write(z)
