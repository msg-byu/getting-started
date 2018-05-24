# Getting Started

A guide to getting started in the Materials Simulation Group (MSG)
with python, Travis CI, Sphinx, GitHub and general scientific
computing. This guide doesn't assume any prior programming experience.  

What follows is meant to be an introduction to the tools and skills
you need to be an effective member of the MSG group and to become a
good programmer. You will be able to modify and adapt most of the
activities to fit your own circumstances once you get familiar with
the tools. However, the overall work flow and design
process are not optional---they are the keys to writing good
scientific code.

This repository contains sample code and input files that you can use
as templates for your own project. However, when it comes to writing
the small amounts of code suggested in the guide, we recommend strongly that you
write it yourself to get practice. Don't just copy the existing
files.

We also recommend that you not skip any sections in this walk-through,
even if you are already familiar with the concepts.

#### Table of Contents

[The Goal of this Repository](#the-goal)

[Computer Setup](#computer-setup)
  * [Github](#github)
    * [Introduction to GitHub](instructions/github.md#introduction)
    * [Create a Repository](instructions/github.md#create-a-repository)
    * [Braches and Code Stability](instructions/github.md#branches-and-code-stability)
    * [Cloning Repositories](instructions/github.md#cloning-repositories)
    
  * [Python](#python)
    * [Docker](#docker)

[Your First Python Code](#your-first-python-code)
  * [Python Packages](#python-packages)
    * [Introduction to Python Packages](instructions/python_packages.md#introduction)
    * [Setting Up Your Package](instructions/python_packages.md#setting-up-your-package)
      * [Setup.cfg](instructions/python_packages.md#setupcfg)
      * [Setup.py](instructions/python_packages.md#setuppy)
      
    * [Testing Your Package](instructions/python_packages.md#testing-your-package)
    
  * [Your First Code](#your-first-code)
    * [Code Documentation](instructions/first_code.md#code-review-and-documentation)
    * [Writing unit-tests](instructions/first_code.md#writing-unit-tests)
    * [Tox](instructions/first_code.md#tox)
    * [Test-driven Development](instructions/first_code.md#tests-driven-development)
      * [Your Second Function](instructions/first_code.md#your-second-function)
      * [Test, Fix, Repeat](instructions/first_code.md#test-fix-repeat)
      
    * [Test-driven Workflow](instructions/first_code.md#overview)

[Continuous Integration, Code Coverage, and Quality](#continuous-integration-code-coverage-and-quality)
  * [Continuous Integration, Travis CI](#continuous-integration-travis-ci)
    * [Build Status Badge](#build-status-badge)
  * [Code Coverage, Codecov](#code-coverage-codecov)
    * [CodeCov Badge](#codecov-badge)
  * [Code Quality, Landscape](#code-quality-landscape)
    * [Code Quality Badge](#code-quality-badge)
    
[API Documentation](#api-documentation)
  * [Sphinx](#sphinx)
  * [GitHub Pages](#github-pages)

[HISTORY.md and your First Commit](#historymd-and-your-first-commit)

## The Goal

If you are interested in joining the group, download the one of the
chapters of [Giordano's "Computational Physics"](http://msg.byu.edu/exercises/) book and use the problems
in the book to practice the steps below.

Your task, once you download the description of the example problems, is to code them up as
a python package with a full suite of [unit
tests](https://en.wikipedia.org/wiki/Unit_testing) on a [continuous
integration](https://en.wikipedia.org/wiki/Continuous_integration)
(CI) server, 100% [test
coverage](https://en.wikipedia.org/wiki/Code_coverage), and [API
documentation](https://en.wikipedia.org/wiki/Application_programming_interface). If
you don't know what any of these things mean feel free to follow the
links, or sit tight. They should become clear as we cover each topic
in this walk-through.

In addition, you will be putting your code up on
[GitHub](https://github.com/) and learning the basics of git to create
a repository that will look somewhat similar to this one when you are
done.

## Computer Setup

### Github

Before we do anything on your local computer you need to get a GitHub
account and make a repository. The directions
[here](instructions/github.md) will walk you through the process.

[Here](https://try.github.io/levels/1/challenges/1) is a good interactive tutorial on git.

### Python

In this group we write most of our code in
[python](https://www.python.org/), if we need it to be faster then we
prototype it in python and then code it in
[fortran](https://en.wikipedia.org/wiki/Fortran). That being said we
execute most of our code from the terminal; 
to work effectively in computational science, you should get used to working in the terminal. If you are a
Windows user we strongly recommend you get
[docker](https://www.docker.com/) for this reason (our group doesn't have expertise in Windows---it's not a friendly OS for computation). If you are a
mac user all you need is to ensure that you have python installed on
your machine, however, you should still get
[docker](https://www.docker.com/).

#### Docker

Once you have docker go to your terminal, or the docker terminal and
pull our python docker image using the following:

```
docker pull wsmorgan/python
```

(Note: This is a rather large download, about 400 MB total.)
This image has working copies of python 2.7, 3.4, 3.5, and 3.6. You
are welcome to develop in any of them. To access the image use:

```
docker run --name 'name' --rm -i -t wsmorgan/python bash
```

Where the 'name' variable has be replaced by a name you'll remember
(for the rest of the walk-through the name I will be using is
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

Now that you have a working code base we want to ensure that it
doesn't get messed up as you continue to develop and other people
start to contribute to your project. One way to ensure that new code
revisions don't break your codes functionality is Continuous
Integration (CI). The idea is that every time anyone pushes to your
git repository or submits a pull request the CI service will run all your
unit tests and let you know if they still pass. The CI provider I'll
cover here is called [Travis CI](https://travis-ci.org/).

### Continuous Integration, Travis CI

The first thing you need to do is enable Travis CI to monitor your git
repository and run unit tests when it detects a change. To do that go
to: [https://travis-ci.org/](https://travis-ci.org/) and click on the
'Sign in with GitHub' or 'Sign up' buttons (either will have the same
effect. Once logged in the server should automatically start linking
with GitHub and listing your repositories, if it doesn't go up to your
name in the top right corner and click on the accounts option that
pops down.

Once your account has synced with GitHub you should see the repository
you created at the start of this project with grey box and `x` in a
square next to it. Click that box, it will turn blue and, the `x` will
turn into a check and viola, you've enabled Travis CI to monitor and
run the unit tests on your repository.

Now we just need to make sure Travis CI knows what to do when it's
running those tests. This is accomplished via the
[.travis.yml](.travis.yml) file. The .travis.yml file should look like:

```
language: python
python:
  - "2.7"
  - "3.4"
# command to install dependencies
install:
  - pip install .
  - pip install tox
# command to run tests
script: tox  
```

The first line of the file tells Travis CI that the programming
language in use is python. Then the lines:

```
python:
  - "2.7"
  - "3.4"
```

Inform Travis CI that you will be performing tests in the python 2.7
and 3.4 environments, if these are not the python versions you want
Travis CI to run tests in then modify these lines to reflect the
python versions you are testing your code in. The next lines tell
Travis CI what it needs to install to run your tests:

```
install:
  - pip install .
  - pip install tox
```

The `pip install .` says to install the local python package once its
been pulled to the server. Then Travis CI is told it needs to install
tox to run the tests (`pip install tox`). This format assumes that
everything your package, and its unit-tests, need to run are included
in your [setup.py](instructions/python_packages.md#setuppy) file. If
this is not the case you will need to list any additional dependencies
for your package in a another file, usually called
`requirements.txt`. The `requirements.txt` file lists each additional
python package needed for your package, or its tests, on a separate
line. For example, if your package needs numpy and scipy, and they
aren't listed in your setup.py, then your `requirements.txt` file
would look like:

```
numpy
scipy
```

With this file in existence you will also need to add this line:

```
  - pip install -r requirements.txt
```

to your .travis.yml after ` - pip install tox`. The last line in the
.travis.yml file tells Travis CI what commands to run in order to
perform the unit-tests:

```
script: tox
```

Since our tests are being performed by tox we're done. If you want to
use something other than tox, like pytest for example, then you would
replace tox with pytest.

#### Build Status Badge

To get the build status badge, which tells users if your code passes
your unit tests, on your README go to travisci.org then select your
repository from the list. Then next your repository name, in the
middle of the screen, you will see the word `build` in a black box
with another box next to it, click on the word build. A pop-up will
open, from the second drop-down menu select Markdown then copy the text
in the box at the bottom of the pop-up. Past that text to the top of
your README.

### Code Coverage, Codecov

Code coverage is a report of how many lines of code your unit-tests
cover. Your goal is to have 100% code coverage for any code you
write. There is a caveat to this idea, there are times when you will
write code that Travis CI cannot test, for example:

```
    def _run_from_ipython(self):
        try: #pragma: no cover
            __IPYTHON__
            self._in_ipython  = True
        except NameError:
            self._in_ipython = False
```

The above function tests to see if the user is executing the code from
an interactive python notebook. Since our unit tests don't run from an
interactive notebook this code will never be executed by the tests. In
this case we can use the comment `#pragma: no cover` as a comment
after the first line of the loop or conditional that won't be
tested. If you recall this same line appeared in our
[setup.cfg](instructions/python_packages.md#setupcfg) file under the
`[coverage:report]` section. That is because the `[coverage:report]`
section of setup.cfg tells coverage, a python package that writes code
coverage reports, which things it should ignore. As you may also
recall `raise AssertionError` and `raise NotImplementedError` were
also excluded from coverage. Ultimately this ability to have code be
ignored for a coverage report should be used sparingly and only when
you have extremely good reason (it is also a good idea to state the
reason as a comment in the code).

To make the reports produced by coverage easier to read we're going to
use a service called [CodeCov](https://codecov.io/). Go to
[https://codecov.io/](https://codecov.io/) and click `Sign up` then
`sign up with GihHub`. Once inside navigate your way to your
repositories list, it should be empty, then click `Add new
repository`. A list of all your repositories should appear, click on
the repository you made for this project and a 2 step process will
appear on the screen. Step one will have a token for you to copy, go
ahead and copy it, you can follow the link of examples in for
uploading the reports but since I'm about to tell you how to do that
it's completely optional. Now go to your `tox.ini` file and add the
following to the bottom of the file:

```
    codecov --token='past your token here'
```

That's it. With that last line added Travis CI will now send your
coverage report to CodeCov after each unit tests it runs.

When CodeCov generates a coverage report it tells you the total amount
of your code that was hit by unit-tests, gives a breakdown of the
coverage of each file and will even go through the code line by line
and highlight in red the lines that you have missed.

#### CodeCov Badge

To add the CodeCov badge to your README go to your repository on
codecov.io then click on settings. On the left you'll see a `Badge`
option, click on it then copy the text under `Markdown`. Paste that
text to the top of your README.md right after the build status badge.

### Code Quality, Landscape

The last issue to be concerned with now that our code will be run
through a CI server and we'll be receiving coverage reports is if our
code is good quality. In other words, does our code follow standard
style guidelines, does it have any sections that are likely to break or
introduce bugs, is it easily readable.... Being able to produce good
quality code will often set you apart as a programmer. There are a
number of sites that perform code quality checks but we're going to
talk about how to use only one of them,
[Landscape](https://landscape.io/). Go to
[https://landscape.io/](https://landscape.io/) and click `Sign in with
GitHub`. On the next screen click `+ Add Repository` then from the
list of your repositories select the repository you created for this
project then click `Add Repositories` at the bottom of the page.

Just like Travis CI, Landscape will monitor your repository and run
checks of your code quality every time you push to GitHub. You can
then review the reports it generates and make improvements as you go.
Down the road, as you grow as a programmer, you may find that
Landscape will throw errors about code you know to be fine, in such
cases you should read up on the
[.landscape.yml](https://docs.landscape.io/configuration.html) file
and use it to refine the checks Landscape is performing.

#### Code Quality Badge

To get the code quality badge to appear on your README go to
Landscapes Dashboard then click on the repository. There will be a
grey box that says `health unknown` in the upper write of the
screen. Click on it, a list of options will appear for style, pick one
you like then go to where you see `Markdown` copy the text below and
paste it to the top of your README.md file right after the text for
the code coverage and build.

## API Documentation

API documentation, Application Programming Interface documentation,
describes to users of your code base how it works and gives examples
of code usage. If you've been following the instructions in this
walk-through then you've already got documentation built into your
python code. If not then go back to [Code
Documentation](instructions/first_code.md#code-review-and-documentation)
and add it in. Then copy all your code into your docker container as
you did in [python package
setup](instructions/python_packages.md#testing-your-package).

### Sphinx

Once in your docker container navigate into your project:

```
cd 'git_repo'
```

Now we are going to use [Sphinx](http://www.sphinx-doc.org/en/stable/)
to build your documentation. In the terminal type:

```
sphinx-quickstart
```

Sphinx will start and prompt you through questions. The first is
asking you where you want the information sphinx makes for you to
go. If directory doesn't exist sphinx can make it. Tell Sphinx to put
the documentation in `docs` then press enter.

Next is a question about how to construct the build directory. This
won't make much difference but go ahead and stick with the default
settings (n or just push enter). Go with the default on the next field
as well. Now Sphinx wants to know things about you and your project,
give it the appropriate entries (when it asks for project version use
0.0 and 0.0.1 for the release).

For the rest of the questions it's best to stick with Sphinx's default
values for now, you can feel free to experiment with them later. There
are 2 exceptions, The first is that you want to enable the sphinx
autodoc extension. So when sphinx asks you `autodoc: automatically
insert docstrings from modules (y/n)` (this happens right after it
asks about 'epub') type `y` for yes. The second is you want to create
a .nojekyll file, this prompt will come up as `githubpages: create
.nojekyll file to publish the document in GitHub pages (y/n)` here say
yes to create the `.nojekyll` file (this file changes how things look
for GitHub).

For the last two prompts you can say yes (the default) to each build
option but we won't be using the windows command file in this tutorial
so you really don't need it.

Now we need to do as Sphinx suggests and:

```
You should now populate your master file docs/index.rst and create
other documentation source files.
```

So open up your master file (emacs is installed in the docker
container) located at docs/[index.rst](docs/index.rst). For now we'll simply add a
single code block to the master file right after it has:

```
.. toctree::
   :maxdepth: 2
```

We want to add code that will tell Sphinx to include our `trial.py`
file in the documentation. To do this add the lines (replace demo with
your package name and for ease of reading I recommend leaving a blank
line between the lines you add and the `:maxdepth: 2` line):

```
.. automodule :: demo.trial
   :members:
```

This code simply informs the make file to automatically add
documentation for the trial module to the documentation site. With that
done type:

```
cd docs
make html
```

There are many different options for building your API documentation,
for an example of a different setup see [aflow's docs
folder](https://github.com/rosenbrockc/aflow/tree/master/docs), as you
get more experience you should experiment with what you want your
documentation to look like. When the make has finished we're going to
copy the entire project back over to your home machine. When you do
this make sure you are in the directory that contains your GitHub
repository's folder, in other words if use:

```
ls
```

You should see the repository file name listed. If not get to that
point then use:

```
docker cp trial:'git_repo' .
```

When this is done you will have a new folder in your repository called
docs. You can now open your documentation using:

```
open 'get_repo/docs/_build/index.html
```

If this doesn't work don't worry, we're going to make it so that
anyone can view the nice API documentation that Sphinx built for you.

### GitHub Pages

GitHub pages is an alternative form of GitHub repository that enables
GitHub to act as a server for static files. To create your GitHub
pages repository go to [GitHub](https://github.com/) and create a new
repository. This repositories name will be special it needs to be
`'your GitHub user name'.github.io`. Go ahead and give the repository a
license and a .gitignore file though it technically won't need
it. Then clone the repository to your local machine just like you did
in the [Cloning
Repositories](instructions/github.md#cloning-repositories) section of
this tutorial. DO NOT clone this repository into your project
repository. I recommend placing it next to, or on the same level as or
in the same folder as, your project repository.

Now do the following:

```
cd 'your GitHub user name'.github.io
touch .nojekyll
mkdir 'your project name'
cp -r ../'git_repo'/docs/_build/* 'your project name'/.
```

Where 'your project name' should be the name of your python package,
'git_repo' is your git repositories name, and 'your GitHub user name'
should be your GitHub user name. Now type:

```
git add .
git commit -m "Added API documentation for 'your project name'."
git push
```

GitHub will then prompt you for your user name and password. Now go
back to your GitHub account and click on your github.io
repository. The changes you made on your local machine should now be
there. What you just did was add all the files in your local copy of
the repository to the git repository using `git add .` (you can also
add files individually by listing them after the add keyword), then you
committed them for a push using `git commit -m "Some message."` (the -m
tells git that you have a message to add, if you don't use the -m then
git will open an editor of some kind for you to add a message anyway),
then finally you pushed the changes up to GitHub.

Now to make your API documentation findable to the general public we
want to add the following line to your 'README.md' file (it can go
anywhere some developers put it at the bottom of the file some near
the top, it's up to you):

``` 
Full API Documentation available at: [github pages](https://'your
GitHub user name'.github.io/'your project name/).  
```

Make sure that the project name matches the folder name your created
in your github.io repository. With that addition your API documentation
will be readable when you make a push at the end of the next section.

## HISTORY.md and Your First Commit

Now that you have [code](#your-first-code),
[unit-tests](instructions/first_code.md#test-driven-development),
[CI](#continuous-integration-travis-ci), [code
coverage](#code-coverage-codecov), [code
quality](#code-quality-landscape) and [API
documentation](#api-documentation) we are almost ready to make your
first commit to GitHub for this project. All we need to do is create a
HISTORY.md file.

The HISTORY.md file contains the revision history for your code. Go
ahead and create the file then add the following to it:

```
# Revision History for "your project"

## Revision 0.0.1
- Initial code commit of trial.py.
- Updated README.md to have API Documentation link, and badges for
  build status, code coverage, and code quality.
- Added files for Travis CI.
- Added files to create python package.
```

Anytime you change your code base you should increment your code
version and record the changes in your HISTORY.md file. This helps
other developers now haw you code changed over time and track places
where the code may have broken.

Now use:

```
git branch
```

To ensure that you are on your development (dev) branch. If you aren't then use:

```
git fetch
git checkout dev
git branch
```

Now use:

```
git add .
git commit -m "Update to revision 0.0.1. See HISTORY.md"
git push
```

Now go to [GitHub](https://github.com/) and click on your project's
repository. Since GitHub automatically takes you to the master branch
nothing will look different. To see your changes click on the
`Branch: master` button and select 'dev' from the drop-down menu. Now
all your changes should be visible. To add these changes to your master
branch we're going to use a pull request. Near the top of the list of
files for your repository there should be a line that says something
like `this branch is 1 commit ahead of master` then a button that says
create pull request. Click the button, on the next page find the
button that says `submit pull request`. Now we wait. Come back to your
repository in 10-15 minutes and click on the pull request tab near the
top. Your new pull request will be listed, click on it. There should
be a report from Travis CI, CodeCov, and Landscape shown, if you
passed all three checks (CodeCov may have encountered an error on this
initial run but that's okay) then push `merge pull request` otherwise
wait a few more minutes that check again. 

Once you've merged the pull request you should see three badges appear
on your repositories README If any of them don't have the word
'passing' or '100%' in them then figure out why and fix them.

The beauty of this approach is that it enables you to use services
like Travis CI and CodeCov to ensure that your collaborators aren't
damaging your code. In that vane you should also always be pushing
changes to a development branch then using pull requests to merge in
changes when they are ready for public use.

That's it. You now have all the tools you need to complete your
assignment from Dr. Hart (as far as project development is
considered). Good luck!

