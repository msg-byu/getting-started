#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(name='',
      version='',
      description='',
      long_description= "" if not path.isfile("README.md") else read_md('README.md'),
      author='',
      author_email='',
      url='',
      license='',
      setup_requires=['pytest-runner',],
      tests_require=['pytest', 'python-coveralls'],
      install_requires=[
          "numpy",
      ],
      packages=[''],
      # scripts=[''],
      include_package_data=True,
      classifiers=[
          'Development Status :: 1 - planning',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
      ],
     )
