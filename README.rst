A set of tools that can be used to simplify python project management
---------------------------------------------------------------------

These tools are designed to work in conjunction with pipenv but they may
also work with traditional setuptools projects. To use these tools do
the following:

1. Add this project as a submodule to your project by executing the
   following on the root of your project

::

    git submodule add https://www.github.com/yasserfarouk/yprojhelpers yprojhelpers
    git submodule init
    git submodule update --recursive

1. Initialize the helpers by running

::

    python yprojhelpers/init_helpers.py

Now you are ready to use the tools for managing your project. The main
services provided are:

-  Converting your README file to reStructuredText format to be usable
   in pypi. To do that run:

::

    python yprojhelpers/init_helpers.py

-  Pumping the version number. That is necessary when you want to make a
   new upload to pypi

::

    python yprojhelpers/pump_version_number.py

-  Updating your documents. We use Sphinx and support both
   reSructuredText and Numpy/Google formats for docs. Noticet that the
   generated documentations will only have doc-string based docs and you
   have to add your own documentation as needed

::

    python update_doc.py

-  This is the *most important script* and it uploads the project to
   pypi making it installable using pip install.

::

    python yprojtools/pypi.py
