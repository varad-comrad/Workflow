# Workflow (WIP)
Scripts to reduce workflow boilerplate for devs, capable of creating new projects, git pushing it, creating new bash functions and so on. For now it only works for python projects.


## INSTALLATION

On a new terminal, write:
```shell
git clone https://github.com/varad-comrad/Workflow
cd Workflow
python workflow/setup.py
```

After finished customizing workflow and double checking if conda did not break anything in bashrc (or variant), you can delete the cloned repo and restart the terminal, and workflow will already be functioning properly

## USAGE (as of now):
- Calling 'workflow' by itself will create a new workflow shell, where all commands can be executed
- It is also possible to call 'workflow' with arguments. The possibilities are:
    - workflow mkdir {args} => mkdirproj.py {args}
    - workflow mkdb {args} => mkdb.py {args}
    - workflow pythonproj {args} => pythonproj.py {args}
    - workflow config {args} => config.py {args}
    - workflow new {args} => make_workflow.py {args}

## TODO Prototype:

- Debug mkdirproj.py, config.py and pyproj.py
- Include code builder, code tester and code benchmarker in coderunner.py
- Debug shell.py methods (90% done)
- Further develop project creation through their kind (data science, web app, etc)

## TODO Phase 1:

- Finish poetry management in pyproj.py
- Debug -h arg in pyproj.py (possibly shell related)
- javaproj.py, cppproj.py
- Documentation

## FUTURE:

- Possibly manage .NET/Node projects as well
- Possibly manage C/C++ projects
- Study possibility of integration with docker
- Auto-installation of a lot of things (conda, docker, make, cmake, etc)

Longer Future: explore possibilitites like AI helper, integration with other CLI tools (Terraform, Ansible), etc.

## REQUIREMENTS:


- Any Linux Distro that supports zsh, bash, dash, fish, ksh, csh or tcsh<!--.  If you're still using other low tier OS, do yourself a favor  -->
- Python3.11+

## DOCUMENTATION: 

Documentation is yet to exist. It will be accessed through [here](https://github.com/varad-comrad/Workflow/docs)

