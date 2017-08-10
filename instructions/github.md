# GitHub

To make a github account to to [github](https://github.com/) and click
sign up for Github, create your user name and password and your all
set. Most, if not all, of the code you write as part of this group
will be maintained on github so learning git will be an important in
your development.

Once you have logged into github create a new repository by clicking
on the plus sign on the top right of the window and clicking on 'Now
repository' from the dropdown menu. You now need to give the
repository a name, you can give it any name you like but I would
recomend something related to the exercise you've been given by
Dr. Hart. You should also give it a description, again whatever you
like but it should reflect what the code you are going to write will
do. Ensure that the Public option is checked and check the box next to
`Initialize this repository with a README'.

Before you click 'Create repository' you should also select the
'Python' option from the 'Add .gitignore' dropdown menu and select a
[license](https://choosealicense.com/) (I recommend the MIT license
for most purposes) from the 'Add a license' dropdown menu. The
.gitignore file tells git which files to automacially ignore when
adding files from your local machine to the github repository. The
license lets other people know how they are allowed to use your code.

Once you've entered values into all the fields you can push `Create
repository'. This repository is where you will store all the code you
create for the exercise you have been assigned. We will now copy this
repository to your local machine so you can add to it. Open your
terminal, or command prompt/[Cygwin](https://www.cygwin.com/) for
windows, and use the `cd` command to move to a place on your system
that you want to store your code (I would recommend making a seperate
directory for all your codes called codes).

Once you are in the desired location click the green 'Clone or
download' button and copy the address it shows you. Then in the
terminal type:

```
git clone (past what you copied from github here)
```

this will clone the repository to your local machine. Now use:

```
cd git_repo
```

to navigate into the newly created folder.

