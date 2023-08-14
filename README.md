# Workflow (WIP)
Scripts capable of creating new projects or pulling it from github with 2 or 3 commands. For now it only works for python projects.
Also capable of creating new shell functions 

Primary goal for now: create mkproj, mkdirproj and mkdb so that it is possible to generate any software dev/data scientist project in 3 shell commands. The projects will always be modularized


## INSTALLATION

On a new terminal, write:
```shell
git clone https://github.com/varad-comrad/Workflow
cd Workflow
python workflow/setup.py
```

Now, you can delete the cloned repo and restart the terminal, and workflow will already be functioning properly

## USAGE (as of now):
- Calling 'workflow' by itself will create a new workflow shell, where all commands can be executed
- It is also possible to call 'workflow' with arguments. The possibilities are:
    - workflow mkdir {args} => mkdirproj.py {args}
    - workflow mkdb {args} => mkdb.py {args}
    - workflow pythonproj {args} => pythonproj.py {args}
    - workflow config {args} => config.py {args}
    - workflow new {args} => make_workflow.py {args}

## TODO:

- Drop version requirement if venv manager is conda and arg -e is passed
- Debug auto-install dependencies for venvs (colorama, cmd2)
- Debug auto-install text_files
- Syntax highlighting for shell.py commands
- Implementation of shell.py methods

## FUTURE:

- In the future, it will be possible to create projects from other languages like Java and Rust
- Eventually projects will also be created through their kind (data science, web app, etc)
- Possibly manage .NET/Node projects as well
- Possibly manage C/C++ projects
- Study possibility of integration with docker
- Study possibility of auto-installing pyenv, if not yet installed

Longer Future: explore possibilitites like AI helper, integration with other CLI tools, etc.

## REQUIREMENTS:


- Any Linux Distro that supports zsh, bash, dash, fish, ksh, csh or tcsh<!--.  If you're still using other low tier OS, do yourself a favor  -->
- cmd2 Python library (```pip install cmd2```)
- colorama Python library (```pip install colorama```)
- Python3.10+
- For Python projects:
    - pyenv (pyenv-virtualenv), poetry or conda

