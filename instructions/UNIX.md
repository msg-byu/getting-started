## File Navigation

As previously mentioned, a lot of work in this team is done directly in the terminal. However, we will be working on multiple files, and these files are sometimes in different folders. To work with this, there are a few commands in the terminal that you need to become very comfortable with in order to navigate. Make sure you know the difference between a file and a folder!

### pwd and ls

`pwd` is quite straightforward. It stands for "print working directory" and it tells you what folder you are currently in. `ls` stands for "list segments" and tells you all files and folders in the folder you are in. For example, if you were in your home folder, and you were to type:

```
pwd
```

the terminal would return something like

```
/home/User
```

and if you were to then type

```
ls
```

the terminal would return folders like:

```
Documents Pictures  Desktop Downloads Music Videos
```

Which you probably recognize as the folders you always see when you first open the file explorer application.

### cd

`cd` stands for "change directory" and is crucial to navigating through your files.

If, from your home directory you want to move into your Documents folder, you would type:

```
cd Documents
```

If you're uncertain whether or not it worked, use `pwd` to double check. 

If you wish to move up a file (for example, documents back to your home directory), the name for one file up is ../

```
cd ../
```

will get you back to the home directory from here. ./ is used to denote the directory you are currently in, which can be very helpful, but not when you're using cd (who changes their directory to the one they're currently in?)

#### Tab

The Tab key could very well become your best friend. Say you needed to navigate into a folder called Ridiculously_long_folder_name_with_a_bunch_of_random_numbers_I_never_remember_the_Order_of_andtheCapitalizationandspacesare_inconsistent987329465592173494587. No one wants to type that much just to navigate one folder. But, if you just type "cd Ridi*tab* and you don't have any other folders in that directory that start "Ridi", the terminal will fill in the rest. Also, never name your folder that. Just don't.

### mkdir and rmdir

`mkdir` is an abbreviation for "make directory" and allows you to create a new folder to start working with. As Dr. Hart suggests you should have a folder called Codes for the work you do on this team, you would do so by typing:

```
mkdir Codes
```

To verify that to folder was made, you can use `ls` to see if it worked.

If you just did that following the instructions but realize now that you actually already had a spot set aside where you wanted to put your codes, you can remove it with the `rmdir` command:

```
rmdir Codes
```

check with `ls` and it should be gone!
 
Feel free to play around with these commands until you feel comfortable navigating the terminal. Once you're ready, head back to cloning your repository by clicking [here](https://github.com/msg-byu/getting-started/blob/master/instructions/github.md)
