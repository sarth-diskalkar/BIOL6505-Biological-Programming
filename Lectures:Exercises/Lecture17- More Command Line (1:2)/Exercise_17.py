"""
Exercise 18: Command Line I
"""

import subprocess
import os

"""
1. Basics

Use the subprocess.run function to execute the following basic CLI commands. If any of these commands are unfamiliar, 
look them up. If you are on a windows machine, ensure you are using WSL or an equivalent. Feel free to complete this 
section intereactively (i.e., by opening a python console, importing subprocess, and using subprocess.run to execute
each of the following commands)

ls
la -a
ls -l
pwd
find . -name '*.py'
df -h
du -h
uname
hostname
printenv
"""



"""
2. Spawning an Intermediate Shell

If you use subprocess frequently, you will eventually realize that a command run through subprocess does not always 
behave the same as a command typed directly into the command line. The reasons for this are a bit nuanced, but we can
generally get around this using the shell=True keyword. This will open an intermediate shell and pass the command
through it, rather than directly calling the associated built-in. Note that, when using shell=True, we pass the command
as a single string, rather than as a list of strings. To see why this can be useful, compare the output of the following
commands:

subprocess.run(['echo', '$PATH'])
subprocess.run('echo $PATH', shell=True)
"""


"""
shell=True can also be used to chain multiple commands together by separating each command with a semicolon like so:

subprocess.run('command 1; command 2; command 3', shell=True)

Use this approach to chain the following commands:
echo output_1
ls
cd ..
echo outut_2
ls

Compare this to the results when you run each command separately, like so:
subprocess.run('echo output_1', shell=True)
subprocess.run('ls', shell=True)
subprocess.run('cd ..', shell=True)
subprocess.run('echo output_2', shell=True)
subprocess.run('ls', shell=True)
"""


"""
Aside: As a word of caution, using shell=True flippantly can create a security vulnerability if you are constructing the 
command from user input. For example, the following code-block:

cmnd = input()
subprocess.run(cmnd, shell=True)

might seem like a useful construction, but it creates a major shell-injection vulnerability. This might not be a problem
if you are the only user, but quickly becomes dangerous if, for example, this code is part of an app with a publicly
accessible web GUI. Maybe your users will only run the commands you intended. Or maybe they'll force delete your root 
directory, or use wget to download malware, or drop a fork bomb into the shell that crashes your entire server. In
short, use shell=True with caution. 
"""

"""
3. Capturing output

Often, we want to capture the output from our command and use it later in our python script. Use subprocess.run()
to capture the output of the ls command, and save it as output. Then print output.stderr, output.stdout, and
output.returncode. Store output.stdout as "dir_contents", and use string operations to separate this string into
a list of strings, with each string corresponding to a single file or directory name. Don't forget to decode stdout
"""



"""
4. Error handling

Sometimes a function runs successfully and sometimes there is an error. Use subrocess to run the following commands. 
1) Create a directory called 'tempdir' using the mkdir command and a file called 'tempfile.txt' with the touch command
2) Create a function that will take user input to delete a file. This should run the rm command without using the -r flag.
   If the user gives a file it should delete succesfully, but if the user gives a directory there should be an error.
   Determine if the function runs successfully and if there is an error, let the user know that they cannot delete a directory
"""



"""
5. Piping
In the lecture, we went over how to pipe two functions together. Use a combination of ls -la and grep to return all of the 
subdirectories in a directory. Now run this code in Python using Popen
"""

