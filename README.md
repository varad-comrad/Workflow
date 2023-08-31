# Workflow (WIP)
Scripts to reduce workflow boilerplate for devs, capable of creating new projects, git pushing it, creating new bash functions and so on. For now it only works for python projects.

Primary goal for now: create mkproj, mkdirproj and mkdb so that it is possible to generate any software dev/data scientist project in 3 shell commands. The projects will always be modularized


## INSTALLATION

On a new terminal, write:
```shell
git clone https://github.com/varad-comrad/Workflow
cd Workflow
python workflow/setup.py
```

After finished customizing workflow, you can delete the cloned repo and restart the terminal, and workflow will already be functioning properly

## USAGE (as of now):
- Calling 'workflow' by itself will create a new workflow shell, where all commands can be executed
- It is also possible to call 'workflow' with arguments. The possibilities are:
    - workflow mkdir {args} => mkdirproj.py {args}
    - workflow mkdb {args} => mkdb.py {args}
    - workflow pythonproj {args} => pythonproj.py {args}
    - workflow config {args} => config.py {args}
    - workflow new {args} => make_workflow.py {args}

## TODO:

- Include code builder, code tester and code benchmarker in coderunner.py
- Auto-install cmd2 and colorama
- Debug auto-installation of pyenv
- Finish poetry management in pyproj.py
- Debug shell.py methods (90% done)
- Syntax highlighting for shell.py commands
- Further develop project creation through their kind (data science, web app, etc)
- Documentation

## FUTURE:

- In the future, it will be possible to create projects from other languages like Java and Rust
- Possibly manage .NET/Node projects as well
- Possibly manage C/C++ projects
- Study possibility of integration with docker
- Auto-installation of a lot of things (conda, docker, make, cmake, etc)

Longer Future: explore possibilitites like AI helper, integration with other CLI tools (Terraform, Ansible), etc.

## REQUIREMENTS:


- Any Linux Distro that supports zsh, bash, dash, fish, ksh, csh or tcsh<!--.  If you're still using other low tier OS, do yourself a favor  -->
- cmd2 Python library (```pip install cmd2```)
- colorama Python library (```pip install colorama```)
- Python3.11+

## DOCUMENTATION: 
### TBA

