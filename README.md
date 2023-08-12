# Workflow (WIP)
simple scripts to automatize some works in zsh

Primary goal for now: create mkproj, mkdirproj and mkdb so that it is possible to generate any software dev/data scientist project in 3 shell commands. The projects will always be modularized


## USAGE (as of now):
- place the workflow directory in your PATH
- call mkdirproj.py for the directory to be created and the text editor called
- call pythonproj.py to set the local python version and virtualenv. 
    - Placing a file and passing it as a second argument to '-s' will automatically pip install the contents of the file
- javaproj, rustproj and mkproj are in progress. mkproj is likely getting deleted in the future

## TODO:

- Refactor pythonproj entirely
- Refactor config.py entirely
- Drop version requirement if venv manager is conda and arg passed is -e

## FUTURE:

Calling 'workflow' by itself will create a new workflow shell, where all commands are executed. Possible solution for the issues related to  venv initialization

All scripts calls will eventually be centralized in a single script called 'workflow', which will also be used to change settings 

Names:
- workflow mkdir => mkdirproj.py
- workflow db => mkdb.py
- workflow python => pythonproj.py
- workflow java => javaproj.py
- workflow rust => rustproj.py

Others: 
- Eventually projects will also be created through their kind (data science, web app, API development, etc)
- Possibly will become a vscode extension as well
- Possibly manage .NET/Node projects as well
- Possibly (unlikely) manage C/C++ projects
- Study possibility of integration with docker
- Study possibility of auto-installing pyenv, if not yet installed
- Consider making classes more API-ish for better customization

Longer Future: explore possibilitites like AI helper, integration with other CLI tools, etc.

## REQUIREMENTS:

- Python3.10+
- For Python projects:
    - virtaulenv (conda or poetry in the future)
    - pyenv
