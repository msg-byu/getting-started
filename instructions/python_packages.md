# Python Packages

#### Table of Contents

[Introduction](#introduction)
[Setting up Your Package](#setting-up-your-package)

[Computer Setup](#computer-setup)

[Your First Python Code](#your-first-python-code)

## Introduction

Python packages are the work horses of python. They are what allow
another user to easily make use of your code. For example type:

```
pip install numpy
```

in your terminal window. This simple command installs the python
package called numpy which contains almost every numerical tool you
will ever need when you program. You can now access the numpy tools
simply by using:

```
import numpy
```

in any of your python scripts. Numpy, and many other packages, are
availabel for anyone to use anywhere through the [python package
index](https://pypi.python.org/pypi). In this walkthrough we will not
be adding your package to the index, but if you build a code that you
feel should be on the index then do so, instructions on how to do that
can be found
[here](http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/contributing.html).


## Setting up Your Package