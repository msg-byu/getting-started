# GitHub

#### Table of Contents

[Introduction](#introduction)

[Create a Repository](#create-a-repository)

[Branches and Code Stability](#branches-and-code-stability)

[Cloning Repositories](#cloning-repositories)

## Introduction

GitHub is a web server that provides version control for software and
code that is being developed. It makes it easy to share code with
people around the world. Most, if not all, of the code you write as
part of this group will be maintained on GitHub so learning git will
be an important in your development. You will use git in the terminal
to interact with GitHub one you are setup.

## Create a Repository

To make a GitHub account go to [GitHub](https://github.com/), click
sign up for GitHub, and create your user name and password. Once you
have logged into GitHub, create a new repository by clicking on the
plus sign on the top right of the window and clicking on 'Now repository'
from the drop-down menu. You now need to give the repository a name.
You can give it any name you’d like, but I would recommend titling it
something related to the exercise you've been given by Dr. Hart. You
should also give it a description. Again this can be whatever you’d
like, but it should reflect what the code you are going to write will
do. Ensure that the Public option is checked and check the box next
to `Initialize this repository with a README’.”

Before you click 'Create repository' you should also select the
'Python' option from the 'Add .gitignore' drop-down menu and select a
[license](https://choosealicense.com/) (I recommend the MIT license
for most purposes) from the 'Add a license' drop-down menu. The
.gitignore file tells git which files to automatically ignore when
adding files from your local machine to the GitHub repository. The
license lets other people know how they are allowed to use your code.

Once you've entered values into all the fields you can push `Create
repository'. This repository is where you will store all the code you
create for the exercise you have been assigned.

## Branches and Code Stability

GitHub not only hosts your code but it will allow you to maintain
multiple versions of your code at the same time. This is extremely
useful when trying to maintain a working and stable code system. For
example lets say you, or someone you collaborate with, are working on
adding new functionality to a code you wrote but accidently introduced
a bug into the code. If you push, git's way of updating the repository
in the server, to the live code copy then anyone who tries to use the
code will experience the bug. That is why it is always a good idea to
create a development branch for your codes and only push changes to
that version. Later when you are sure the code works (via unit testing
and continuous integration) you can use what's called a pull request
to merge the changes into your main repository.

To help you get into the habit of working on a development branch
let's create one for your new repository. On the repository home page
you should see a button labeled `Branch: master`. Click on it and in
the text field type the word 'dev'. You should then see new box show
up saying `Create branch dev`. Click on it. You have now created a
development branch to work in.

## Cloning Repositories

We will now copy this repository to your local machine so you can add
to it. Open your terminal, or command
prompt/[Cygwin](https://www.cygwin.com/) for windows, and use the `cd`
command to move to a place on your system that you want to store your
code (I would recommend making a separate directory for all your codes
called codes).

Once you are in the desired location click the green 'Clone or
download' button and copy the address it shows you. Then in the
terminal type:

```
git clone (paste what you copied from GitHub here)
```

this will clone the repository to your local machine. Now use:

```
cd git_repo
```

to navigate into the newly created folder. We want to make sure the
branch we are working on is the dev branch. To see which branch you
are on use:

```
git branch
```

To switch to the dev branch use:

```
git checkout dev
```

We are now working on the dev branch and anything we commit will be
pushed to dev instead of master creating a stable code base.

You are now ready to return to the remainder of the walkthrogh found
[here](../README.md#python).
