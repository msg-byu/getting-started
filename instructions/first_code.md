# Your First Code

#### Table of Contents

[Code Review and Documentation](#code-review-and-documentation)

[Writing unit-tests](#writing-unit-tests)

[Tox](#tox)

[Test-driven Development](#test-driven-development)
  * [Your Second Function](#your-second-function)
  * [Test, Fix, Repeat](#test-fix-repeat)

[Overview](#overview)

## Code Review and Documentation

Your first code was:

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

The first thing that appears is `def square(x):` this defines a
function called square which takes a single argument x. Everything
underneath this definition that is indented is part of the
function. The documentation for the function, all the text in
triple quotes, comes next. This is according to the sphinx google style
documentation. Since documenting code is extremely important I will
explain how it usually works.

Documentation always starts with and ends with three double
quotes and comes immediately after the definition of the function
or class. Everything inside the triple quotes is also often referred to
as a docstring. The first thing inside the documentation is a
brief description of what the function should do. After that the
input, or arguments, of the function are listed below the `Args:`
tag. Each argument is listed so that its name appears first, followed
by it's type in parentheses. After the argument's type should follow a description of
what the argument is, i.e., a number to be squared, a list to be
sorted, an instance of a class ..... Once all the arguments
have been listed, the variables that the function returns also need
to be described using the same format. There is additional information
you can include in the function's documentation, like if it raises
any exception or errors (ValueErrors, TypeErrors, ...). Some examples of this can be found 
[here](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

Once you are done with the documentation, you write your actual code. This
sample function is extremely simple, consisting of a single line of
code, however this will not be the case most of the time.

## Writing unit-tests

Having written this first function we need to test it to ensure it works properly.
We will do that using the python packages tox and pytest.
Tox is a python package that handles unit testing in multiple
python versions ensuring your code will be compatible with the python
versions you desire. Pytest is a package containing many tools that help 
us write unit tests.

To make our first unit test we will go to the directory containing
your setup.py and setup.cfg files. Once there, make a new directory
called tests and navigate into it:

```
mkdir tests
cd tests
```

In this directory we will write all of our codes for testing. Each
testing module or code file that you want tox to find and run needs to
start with the word `test`. For this first test lets make the file
`test_my_pkg.py`. Inside the file write the following code:

```
"""Tests the mathematical functions defined in my_pkg/trial.py
"""

import pytest

def test_square():
    """Tests the squaring function"""

    from my_pkg.trial import square

    assert 4 == square(2)
```

The first thing in our testing code file is a line of documentation
describing what the tests in it will do. While this is optional, it is
generally a good idea as it helps other developers know what is going
on. Next we import pytest and define a function `test_square`. The
name is not arbitrary. Just like the file name for tests, each
function that contains tests also needs to start with the name `test`.
(Anything can come after test.) Otherwise, pytest and tox will not find
the tests when they are run. Inside the function we give a
description of what it will do, then import the function that is
going to be tested:

```
from my_pkg.trial import square
```

Remember to replace my_pkg with your package name. Next we write the
actual test:

```
assert 4 == square(2)
```

The assert in the line of code above checks that any equality or
statement that follows is true. It is possible to include multiple
asserts in a single test function, for example:

```
assert 4 == square(2)
assert 4 == square(-2)
assert 12.25 == square(3.5)
assert 2 == round(square(sqrt(2)), 5)
```

It is usually a good idea to have each test check for a different possible case
where the code could break. For example, here we test to make sure that
our function correctly computes the square of negative numbers, fractions and
irrational numbers. We want to try to make our code fail now so we can correct problems 
sooner and more easily.

## Tox

With this test code written we need to write a file that will tell tox
what to do. Go back up a directory to where setup.py is:

```
cd ../
```

Here we will make a file called [tox.ini](../tox.ini) a sample of which
can be found in the getting_started repository (or by following the
link). The example file looks like this:

```
[tox]
envlist = py27, py34

[testenv]
passenv = TRAVIS TRAVIS_JOB_ID TRAVIS_BRANCH
deps=
    pytest
    coverage
    codecov
commands=
    coverage run --source=my_pkg -m pytest
```

The first two lines of the file tell tox which python environments you
want to test your code in. It's usually a good idea to check that your
code runs in python 2, since many users haven't switched to python 3
yet, and there are a few version of python 3. The sample file tells tox to
run the tests in python 2.7 and python 3.4. Modify this line to test
the python versions you would like to include.

The rest of the code tells tox what it's doing. The first assignment,
`passenv` informs tox that it will (eventually) be run on the [Travis
CI](https://travis-ci.org/) server for continuous integration. We will
discuss how to setup up Travis in a [later
section](../README.md#continuous-integration-code-coverage-and-quality). The
next assignment, `deps` tells tox which packages it will need to run
your tests. In this case we've listed:

 - pytest (which actually runs the tests)
 - coverage (which makes code coverage reports [discussed later](../README.md#continuous-integration-code-coverage-and-quality))
 - codecov (which also handles coverage reports)

Finally we use `commands` to tell tox what it's doing, the command we supply it with
is `coverage run --source=my_pkg -m pytest` (replace my_pkg
with your package name). This tells tox to use the command `coverage
run` on your package (`--source=my_pkg`), with the method pytest (`-m
pytest`). You can use tox.ini to do a lot of other things as well--if
you're interested read the
[documentation](http://tox.readthedocs.io/en/latest/examples.html)--but 
in most cases what you see here is all you will need.

At this point your repository folder should look like this:

```
'my_repo'/'package'/__init__.py
'my_repo'/'package'/trial.py
'my_repo'/setup.py
'my_repo'/setup.cfg
'my_repo'/tests/test_my_pkg.py
'my_repo'/tox.ini
'my_repo'/README.md
'my_repo'/LICENSE
'my_repo'/.gitignore
```

Now we're going to copy your repository to the docker container to run
the tests and make sure that they work (just like you did when testing
your [python package setup](python_packages.md#testing-your-package)):

```
cd ../
docker cp 'my_repo' my_container:.
```

Now go back to the terminal that is running your docker container (if
you exited it earlier you will need to restart it before you can copy
the code over) and type:

```
cd 'my_repo'
tox
```

A bunch of stuff should print to your screen, but we'll just focus on 
the last bit which should say something like this:

```
____________________________________________________________ summary _____________________________________________________________
  py27: commands succeeded
  py34: commands succeeded
  congratulations :)
```

Note that since we tested using python 2.4 and python 3.7, the output 
listed py27 and py34. If you tested different versions of python your code 
should reflect that. If you see any errors at this point, please double check
everything you've done in this section and try again. If it still
won't work please submit an
[issue](https://github.com/msg-byu/getting-started/issues) describing
the error and we'll get back to you ASAP with help. If all went well
then return to your local machine where we will make your second
python function using test-driven development.

## Test-driven Development

The idea behind test driven development is to start by writing tests for
what you want your code to do, and then writing the code so that
it will pass the tests. This makes identifying errors and debugging much
easier. To illustrate how this works we'll write a
second function inside of trial.py using the test-driven framework.

### Your Second Function

Inside of trial.py define a new function called factorial:

```
def factorial(n):
```

The factorial function will find the
factorial of an integer. Let's write the documentation for our
new function:

```
    """Calculates the factorial of the provided integer.

    Args:
        n (int): The value that the factorial will be computed from.

    Returns:
        fact (int): The factorial of n.

    Raises:
        ValueError: If n is not an integer.
    """
```

We've included a raises descriptor in the documentation, since if the
user tries to pass a float (say 3.5) into the function, we want to warn them
of the error rather than try to find the factorial. Now, before we
write a single line of code let's write some unit tests.

Inside of tests/test_my_pkg.py add the following lines of code for
tests. You can add additional tests if you so desire, but make sure you 
at least have these ones:

```
def test_factorial():
    """Tests the factorial function."""

    from my_pkg.trial import factorial

    assert 24 == factorial(4)
    assert 6 == factorial(3.0)
    assert 1 == factorial(0)
    assert 1 == factorial(-1)

    with pytest.raises(ValueError):
        factorial(3.5)        
```

Everything here should look very familiar with the exception of the
lines:

```
    with pytest.raises(ValueError):
        factorial(3.5)        
```

These code lines will check to make sure that a `ValueError` is raised
if the user passes the function a float instead of an int. Now that we
have tests we can go back to our function and finish writing the code:

```
    if not isinstance(n,int):
        raise ValueError("The input to factorial must be an integer.")

    if n < 0:
        fact = 1
    else:
        fact = n
        for i in range(1,n):
            fact = i*fact

    return fact
```

Now we run our unit tests to see if our code
will do what we expect.

### Test, Fix, Repeat

Copy your code into the docker container and run your unit tests just
like you did when making [your first unit-tests](#tox). This time you
should see something that looks like:

```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

n = 3.0

    def factorial(n):
        """Factorial calculates the factorial of the provided integer.

        Args:
            n (int): The value that the factorial will be computed from.

        Returns:
            fact (int): The factorial of n.

        Raises:
            ValueError: If n is not an integer.
        """

        if not isinstance(n,int):
>           raise ValueError("The input to factorial must be an integer.")
E           ValueError: The input to factorial must be an integer.

my_pkg/trial.py:31: ValueError
=============================================== 1 failed, 1 passed in 0.08 seconds ===============================================
ERROR: InvocationError: '/Users/wileymorgan/codes/getting-started/.tox/py34/bin/coverage run --source=my_pkg -m pytest'
____________________________________________________________ summary _____________________________________________________________
ERROR:   py27: commands failed
ERROR:   py34: commands failed
```

Our tests failed! It looks like when we passed in a value of 3.0,
which we know is a valid integer, the
code raised a ValueError. We'll need to fix this. In your code replace:

```
    if not isinstance(n,int):
        raise ValueError("The input to factorial must be an integer.")
```

With:

```
    if not isinstance(n,int):
        if int(n) == n:
            n = int(n)
        else:
            raise ValueError("The input to factorial must be an integer.")
```

Now if the input value isn't an integer, we check to see if the input
value is equivalent to an integer. If it is, we replace it with the 
equivalent integer. With that fixed, let's check to see if we're 
passing all our tests again in the docker container. (Don't forget 
to copy the code you've changed into the container before running `tox`).

The result should be something like:

```
_________________________________________________________ test_factorial _________________________________________________________

    def test_factorial():
        """Tests the factorial function."""

        from my_pkg.trial import factorial

        assert 24 == factorial(4)
        assert 6 == factorial(3.0)
>       assert 1 == factorial(0)
E       assert 1 == 0
E        +  where 0 = <function factorial at 0x1074c81e0>(0)

tests/test_my_pkg.py:20: AssertionError
=============================================== 1 failed, 1 passed in 0.06 seconds ===============================================
ERROR: InvocationError: '/Users/wileymorgan/codes/getting-started/.tox/py34/bin/coverage run --source=my_pkg -m pytest'
____________________________________________________________ summary _____________________________________________________________
ERROR:   py27: commands failed
ERROR:   py34: commands failed
```

We passed the factorial(3.0) test but failed another test now. It
seems that when passed a value of zero the function returns 0 instead
of 1. We'll need to fix this as well so in your code replace:

```
    if n < 0:
        fact = 1
```

With:

```
    if n <= 0:
        fact = 1
```

Now when we copy the revised code to the docker container and run tox we get:

```
==================================================== 2 passed in 0.02 seconds ====================================================
____________________________________________________________ summary _____________________________________________________________
  py27: commands succeeded
  py34: commands succeeded
  congratulations :)
```

## Overview

Just to be clear, the work flow in test-driven development is to decide
what your code should do and write tests to verify
that performance before you write any code. In other words, each time
you start to write a new function you should (1) define the function,
(2) write its documentation, (3) write tests to model the desired output, and only then
(4) write the code. This will ensure that all your functions have unit
tests and that they all behave as expected.

Now that you program in a test-driven way let's move on to [continuous
integration](../README.md#continuous-integration-code-coverage-and-quality)
