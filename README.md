# Getting Started

A guide to getting started in the Materials Simulation Group (MSG)
with python, Travis CI, Sphinx, GitHub and general scientific computing.

What follows is meant to be an introduction to the tools you skills
you need to be an effective member of the MSG group and become a good
programmer. Most of the things is this guide you will be able to
modify and adapt to fit your own circumstances once you get familiar
with the tools. However, the ideas behind the overall work flow and
design process are not optional as they are the keys to writing good
scientific code.

This repository contains sample code and input files that you can use
as templates for your own project, however, when it comes to writing
the small amounts of found here code it is highly recommended that you
write it yourself to get practice instead of just copying the existing
files.

#### Table of Contents

[The Goal of this Repository](#the-goal)

[Computer Setup](#computer-setup)
  * [Github](#github)
  * [Python](#python)

[Your First Python Code](#your-first-python-code)

## The Goal

If you have yet to do so you should contact [Dr. Gus
Hart](http://msg.byu.edu/) to express your interest in joining MSG and
ask him for problems to work through.

Your task, once you have your assigned problems, is to code them up as
a python package with a full suite of [unit
tests](https://en.wikipedia.org/wiki/Unit_testing) on a [continuous
integration](https://en.wikipedia.org/wiki/Continuous_integration)
(CI) server, 100% [test
coverage](https://en.wikipedia.org/wiki/Code_coverage), and [API
documentation](https://en.wikipedia.org/wiki/Application_programming_interface). If
you don't know what any of these things mean feel free to follow the
links, or sit tight. They should become clear as we cover each topic
in this walk through.

In addition you will be putting your code up on
[GitHub](https://github.com/) and learning the basics of git to create
a repository that will look somewhat similar to this one when you are
done.

## Computer Setup

### Github

Before we do anything on your local computer you need to get a GitHub
account and make a repository. The directions
[here](instructions/github.md) will walk you through the process.

### Python

In this group we write most of our code in
[python](https://www.python.org/), if we need it to be faster then we
prototype it in python and then code it in
[fortran](https://en.wikipedia.org/wiki/Fortran). That being said we
execute most of our code from the terminal, to fit into the group with
ease you should also be making use of the terminal. If you are a
Windows or linux user we strongly recommend you get
[docker](https://www.docker.com/) for this reason (we are sick of
trying to make code work on windows and linux machines). If you are a
mac user all you need is to ensure that you have python installed on
your machine, however, you should still get
[docker](https://www.docker.com/).

Once you have docker go to your terminal, or the docker terminal and
pull our python docker image using the following:

```
docker pull wsmorgan/python
```

This image has working copies of python 2.7, 3.4, 3.5, and 3.6. You
are welcome to develop in any of them. To access the image use:

```
docker run --name 'name' --rm -i -t wsmorgan/python bash
```

Where the 'name' variable has be replaced by a name you'll remember
(for the rest of the walk through the name I will be using is
demo). This command creates a docker container with the name you
specify and opens an interactive bash terminal of the docker
image. The '--rm' flag means that when you exit the interactive
terminal the container will also be deleted. We will be using this
docker image through out the rest of this tutorial to run and test any
code you write. You can even develop your code from this container,
however, keep in mind that when you exit the container will be deleted
and any code you have not pushed to GitHub will be lost (even without
the '--rm' flag in the command you risk losing any code you wrote
while in the container). I will assume that you will be producing code
on your machine and that we will be transferring it to the container
when tests need to be run.

In the future, if you are writing a script that will be useful to
others, you may want to consider [creating your own docker
image](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#build-cache)
with your scripts built into it.

## Your First Python Code

Before we even start to write our first program we need to get our
python package setup properly. This will allow us to easily test our
codes as we build them, a process called test driven development, and
ensure the code behaves as we expect.

### Python Packages

To setup your python package follow the instructions found
[here](instructions/python_packages.md).

### Your First Code 

Technically you've already written your first python code during the
process of making and testing your [python
package](instructions/python_packages.md#testing-your-package). We
will briefly go over the contents of that code here and write a unit
tests for it. Then write your second python code and demonstrate what
is called [test-driven
development](https://en.wikipedia.org/wiki/Test-driven_development)
(TDD).

The remaining instructions for this section can be found
[here](instructions/first_code.md).

## Continuous Integration, Code Coverage, and Quality

## API Documentation


