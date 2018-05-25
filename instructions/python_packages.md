# Python Packages

#### Table of Contents

[Introduction](#introduction)

[Setting up Your Package](#setting-up-your-package)
  * [Setup.cfg](#setupcfg)
  * [Setup.py](#setuppy)

[Testing Your Package](#testing-your-package)

## Introduction

Python packages are the work horses of python. They are what allow
another user to easily make use of your code. For example type:

```
pip install numpy
```

in your docker terminal. This simple command installs the python
package called numpy which contains almost every numerical tool you
will ever need when you program. You can now access the numpy tools
simply by using:

```
import numpy
```

in any of your python scripts. Numpy, and many other packages, are
available for anyone to use anywhere through the [python package
index](https://pypi.python.org/pypi) (pypi). In this walk through we
will not be adding your package to the index, but if you build a code
that you feel should be on the index then do so, instructions on how
to do that can be found
[here](http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/contributing.html).


## Setting up Your Package

The first thing to do in setting up your python package is to choose a
package name and create a folder in your repository with that
name. This folder will contain all your python code for this
project. By convention python package names are usually lower case
without spaces, you don't have to follow these conventions but it's a
good idea to keep them in mind in case you do submit a your package to
pypi. In the [sample
repository](https://github.com/msg-byu/getting-started) the package
name is 'my_pkg' so the command would be:

```
mkdir my_pkg
```

Once you've chosen a package name and created the folder you will need
to create a [setup.py](../setup.py) and
[setup.cfg](../setup.cfg). These files tell pip how to install your
package. You will find templates of both files in the sample
repository. You should copy them to your repository so that they are
on the same level as you package directory. You will also want to make
a file `__init__.py` in the package folder, this file will remain
empty during this walk through but it can be used to do some useful
things shorten user imports or import tools for the entire
package. Examples of this can be found
[here](https://github.com/wsmorgan/analyzefit/blob/master/analyzefit/__init__.py).

### Setup.cfg

You should take a good look at setup.cfg but you don't need to modify
it. A lot of what you find inside is related to generating code
coverage from the unit tests. The first two lines establish an alias
for pytest, the lines between `[coverage:report]` and `[coverage:run]`
tell the unit testing package what to ignore or exclude from coverage
reports. We'll talk more about this later when discussing [code
coverage](coverage.md). The last portion, under `[coverage:run]`, lets the unit
testing software know if there are any modules that should be excluded
from a coverage report entirely. For now, and in most cases, you will
leave this blank. If you want to know more about building the
setup.cfg file you can read the python
[documentation](https://docs.python.org/2/distutils/configfile.html).

### Setup.py

You will need to modify setup.py to match you and your package. The
first few lines (everything above `from os import path` on line 19)
make sure that the python packages setuptools and pypandoc exist on
your machine and can be imported. The fields you will need to modify
are all inside the brackets of `setup` found on line 20 and are
indicated by empty quotation marks. In each case you need to enter the
correct information between the quotes, I'll walk you through each value:

```
name=''
```

In this field you should enter the name of your package (for the same
repository this would be ```name='my_pkg'```).

```
version=''
```

Here you enter the current distribution version of your code. The
distribution version takes the form of a period separated list with
entries of major revision, minor revision, and patch revisions. A major
revision occurs when you change how your code works, that is if
someone was using your code before the revision for a project and
attempted to use it the same way afterwards the code would no longer
function. A minor revision is a change in the public API, such as
creating a new subroutine or function that is publicly available. The
patch revisions are small changes to the code to fix issues and
enhance performance. For more information on semantic versioning you
may read [this article](http://semver.org/).

Anytime you change and commit your code to GitHub you should increment
the code version in the appropriate field. Since this is the initial
version of a new code use `0.0.1` for your current version.

```
description=''
```

A brief description of your package.


```
author=''
```

Your name goes here.

```
author_email=''
```

Your email address goes here.

```
url=''
```

Here you should place the link to your GitHub repository for this
project, i.e., 'github.com/"your GitHub user name"/"your GitHub
repository for this project"'.

```
license=''
```

Here you will place the title of the license you've placed in your
GitHub repository for this package. (We usually use MIT but whichever
you choose is fine).

```
install_requires = [
    "numpy",
]
```

You don't need to change anything here yet but you should be aware of
this field. As you build your code you may find yourself making use of
other python packages such as numpy or matplotlib (pythons plotting
package). Any packages your code needs in order to install and run
properly should be listed here as a comma separated list and usually
with each entry on a separate line. For example if matplotlib is being
used by my package this should look like:

```
install_requires = [
    "numpy",
    "matplotlib",
]
```

```
packages = ['']
```

Here you will list the packages (and any sub-packages) this setup.py
file will install. For your purposes as of now it will be sufficient
to put your package name here. If you ever build a more elaborate code
you may need to include multiple packages, for an example of this see
[Fortpy](https://github.com/rosenbrockc/fortpy/blob/master/setup.py).

```
# scripts=['']
```

This is another field that you can ignore for now but should be aware
of. Any scripts, i.e., command line executable programs, you place in
these brackets will get copied to your bin (the place on your computer
where anything you can type into the terminal, like 'cp', lives). Only
ever uncomment this line if you have a script to install, otherwise
setup.py will fail.

```
classifiers=[
    'Development Status :: 1 - planning',
    'Intended Audience :: Science/Research',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
],
```

This field is general information. Options for the values you can use
for each field can be found
[here](https://pypi.python.org/pypi?%3Aaction=list_classifiers). Most
of this can stay the same for you but if you aren't using a mac you
should change the OS and if you aren't using python 2 you should
update the python language version.

This section of your setup.py should now look something like:

```
setup(name='my_pkg',
      version='0.0.1',
      description='Some descriptive words like: This is a demonstrative package.',
      long_description= "" if not path.isfile("README.md") else read_md('README.md'),
      author='you name',
      author_email='your email',
      url='https://github.com/msg-byu/getting-started',
      license='MIT',
      setup_requires=['pytest-runner',],
      tests_require=['pytest', 'python-coveralls'],
      install_requires=[
          "numpy",
      ],
      packages=['my_pkg'],
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

```

## Testing Your Package

At this point you should have a file structure that looks like:

```
'my_repo'/'package'/__init__.py
'my_repo'/setup.py
'my_repo'/setup.cfg
'my_repo'/README.md
'my_repo'/LICENSE
'my_repo'/.gitignore
```

In order to do anything with this package we need to include some
python code. To ensure that everything is working we'll make a test
script, [trial.py](../my_pkg/trial.py), located in the package folder:

```
'my_repo'/'package'/trial.py
```

In the sample repository this code is located at:

```
getting_started/my_pkg/trial.py
```

The contents of trial.py should be:

```
def square(x):
    """Finds the square of the input.

    Args:
        x (float): The number to be squared.

    Returns:
        x2 (float): The squared number.
    """

    return x**2
```

Here we have defined a function that squares a given value. The text
inside of three quotes in this functions is
[documentation](../README.md#your-first-code) which we go into in more
detail later.

Now that we have some code to test with we can install our package and
insure that it functions properly. First we need to copy all our code
to our docker container. To do this you need your docker container
running in one terminal while you use another to copy files to it. If
your docker container is not running then use:

```
docker run --name my_container --rm -i -t wsmorgan/python bash
```

to get it going. Then in your other terminal use navigate to the
folder your git repository is in and use:

```
docker cp 'my_repo' my_pkg:.
```

(where 'my_repo' is the repository file) to copy the repository into
the docker container. Now go back to the terminal that you used
`docker run` in and type `ls`. You should now see your git
repository. Now navigate into the folder `cd 'my_repo'` then enter
the commands (replace my_pkg with your package name):

```
pip install -e .
python
from my_pkg import trial
trial.square(2)
exit()
```

You should have seen the number 4 printed to the screen before you
typed `exit()`. If you didn't or any of these commands gave you errors
stop and go back through this setup to ensure that you have everything
correct. If

```
pip install -e .
```
gives an error, you may have to use

```
pip install --upgrade setuptools
```

If you still have errors, please submit an [issue
here](https://github.com/msg-byu/getting-started/issues) describing
your problem and we'll get back to you ASAP.

What you just did is install a local copy of your package. You only
need to do this once per package because the code python is importing
is now the live version of your code on your machine. Any changes you
make will effect the output immediately.

You have now successfully created your first python package. Please
return to the main [walk through](../README.md#your-first-code).
