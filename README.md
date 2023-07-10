# simple-scripts (WIP)
simple scripts to automatize some works in zsh

Primary goal for now: create mkproj, mkdirproj and mkdb so that it is possible to generate any software dev/data scientist project in 3 shell commands. The projects will always be modularized


## USAGE (as of now):
- place the workflow directory in your PATH
- call mkdirproj.py for the directory to be created and the text editor called
- call pythonproj.py to set the local python version and virtualenv. 
    - Placing a file and passing it as a second argument to '-s' will automatically pip install the contents of the file
- javaproj, rustproj and mkproj are in progress. mkproj is likely getting deleted in the future