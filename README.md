# Workflow (WIP)
Scripts capable of creating new projects or pulling it from github with 2 or 3 commands. For now it only works for python projects.
Also capable of creating new shell functions 

Primary goal for now: create mkproj, mkdirproj and mkdb so that it is possible to generate any software dev/data scientist project in 3 shell commands. The projects will always be modularized


## USAGE (as of now):
- place the workflow directory in your PATH
- Calling 'workflow' by itself will create a new workflow shell, where all commands can be executed
- It is also possible to call 'workflow' with arguments. The possibilities are:
    - workflow mkdir {args} => mkdirproj.py {args}
    - workflow db {args} => mkdb.py {args}
    - workflow pythonproj {args} => pythonproj.py {args}
    - workflow config {args} => config.py {args}
    - workflow new {args} => make_workflow.py {args}

## TODO:

- Drop version requirement if venv manager is conda and arg passed is -e
- Add .gitignore file when -g is passed to mkdirproj.py and initialize it with '.python-version'
- Exploit the \_\_main\_\_.py files

## FUTURE:

- In the future, it will be possible to create projects from other languages like Java and Rust
- Eventually projects will also be created through their kind (data science, web app, API development, etc)
- Possibly manage .NET/Node projects as well
- Possibly manage C/C++ projects
- Study possibility of integration with docker
- Study possibility of auto-installing pyenv, if not yet installed

Longer Future: explore possibilitites like AI helper, integration with other CLI tools, etc.

## REQUIREMENTS:

- Python3.10+
- For Python projects:
    - pyenv (pyenv-virtualenv), poetry or conda
