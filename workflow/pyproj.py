#!/usr/bin/env python
import argparse, subprocess, pathlib, settings, errors


def parse_pyproject():
    parser = argparse.ArgumentParser(usage=errors.newproj_error())
    # requires pyenv to manage python versions
    parser.add_argument('-p', '--python-version', type=str)
    
    parser.add_argument('-n', '--name', type=str, required=True)

    parser.add_argument('-f', '--force-install',
                        default=False, action='store_true')
    # force installation of python version if not present.
    # like previous, requires pyenv.

    parser.add_argument('-e', '--env', type=str)
    # name of venv (if pyenv or conda) TBA poetry.

    parser.add_argument('-s', '--set-new-env', nargs='+', default=[])

    parser.add_argument('-d', '--dir', default='.', type=str)

    parser.add_argument('-ds','--data-science', action='store_true', default=False, required=False)

    parser.add_argument('-wd','--web-dev', action='store_true', default=False, required=False)

    # if user wishes to set new environment. If specified, arguments must be the name of the venv and the path to requirements.txt
    # for pip installation. Second argument is optional. Tool for managing may be conda or poetry or virtualenv.
    # Defined in settings.py

    return parser


class PyProject:
    def __init__(self, parsed_args: argparse.Namespace):
        if parsed_args.set_new_env and len(parsed_args.set_new_env) > 2:
            # change error type later
            raise ValueError(
                'Set new environment must have at most 2 arguments')
        if parsed_args.python_version is None and parsed_args.env == [] and settings.s['venv_manager'] != 'conda':
            raise ValueError("Python version must be specified")
        self.args = parsed_args
        self.cmds: list[str] = [f'cd {self.args.dir}']


    #?#####################################################################################################################


    def manage_version(self):
        if settings.venv_manager == 'conda':
            return self.__manage_version_conda()
        else:
            return self.__manage_version_pyenv()

    def __manage_version_pyenv(self):
        res = subprocess.check_output('pyenv versions', shell=True, cwd=self.args.dir)
        if self.args.python_version not in str(res) and self.args.force_install:
            self.__install_version_pyenv()
        subprocess.run(f'pyenv local {self.args.python_version}', cwd=self.args.dir, shell=True)
        if settings.venv_manager == 'poetry':
            self.cmds.append(f'poetry env use {self.args.python_version}')
        return self

    def __install_version_pyenv(self):
        subprocess.run(
            f'pyenv install {self.args.python_version}', shell=True, cwd=self.args.dir)
    
    def __manage_version_conda(self):
        res = str(subprocess.check_output(f'conda info --envs', shell=True, cwd=self.args.dir))
        if self.args.env and self.args.env in res:
            return self
        subprocess.run(f'conda create python={self.args.python_version} -n {self.args.set_new_env[0]} {settings.s["conda_extension"]}', shell=True)
        return self
    

    #?#####################################################################################################################

    
    def manage_venv(self):
        if settings.venv_manager == 'poetry':
            self.__poetry_venv_manager()
            # self.cmds.append('poetry shell')
        if self.args.env:
            self.__choose_preexisting_venv()
        elif self.args.set_new_env:
            self.__new_venv()
        return self

    def __poetry_venv_manager(self):
        subprocess.run( 
            f"poetry new {settings.s['poetry_extension']} {self.args.name}", shell=True, cwd=self.args.dir)
        # self.__check_dependencies() #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return self

    def __choose_preexisting_venv(self):
        match settings.venv_manager:
            case 'pyenv':
                self.cmds.append(f'pyenv activate {self.args.env}')
            case 'conda':
                self.cmds.append(f'conda activate {self.args.env}')

    def __new_venv(self):
        match settings.venv_manager:
            case 'pyenv':
                subprocess.run(
                    f"pyenv virtualenv {self.args.python_version} '{self.args.set_new_env[0]}'", cwd=self.args.dir, shell=True)
                self.cmds.append(f'pyenv activate {self.args.set_new_env[0]}')
                self.cmds.append(f'pip install colorama cmd2 click')
            case 'conda':
                self.cmds.append(f'conda activate {self.args.set_new_env[0]}')
                self.cmds.append(f'conda install -c conda-forge colorama cmd2 click -y')
        self.__check_dependencies()
        
    def __check_dependencies(self):    
        try:
            path = pathlib.Path(f'./{self.args.set_new_env[1]}')
            if path.exists():
                self.__package_install()

        except IndexError:
            if self.args.data_science:
                self.__install_ds_packages()
            if self.args.web_dev:
                self.__install_wd_packages()

        
    def __package_install(self):
        match settings.venv_manager:
            case 'pyenv':
                self.cmds.append(f'pyenv exec pip install -r {self.args.set_new_env[1]}')
            case 'conda':
                self.cmds.append(f'conda install --file {self.args.set_new_env[1]}')
            case 'poetry':
                #! ############################
                # self.cmds.append(f'pyenv exec pip install -r {self.args.set_new_env[1]}')
                pass


    def __install_ds_packages(self):
        match settings.venv_manager:
            case 'pyenv':
                self.cmds.append(f'pyenv exec pip install -r {settings.s["home_dir"]}/text_files/datascience.txt')
            case 'conda':
                self.cmds.append(
                    f'conda install --file {settings.s["home_dir"]}/text_files/datascience.txt')
            case 'poetry':
                #! ############################
                # self.cmds.append(f'pyenv exec pip install -r {self.args.set_new_env[1]}')
                pass

    def __install_wd_packages(self):
        match settings.venv_manager:
            case 'pyenv':
                self.cmds.append(
                    f"pyenv exec pip install -r {settings.s['home_dir']}/text_files/web.txt")
            case 'conda':
                self.cmds.append(
                    f"conda install --file {settings.s['home_dir']}/text_files/web.txt")
            case 'poetry':
                #! ############################
                # self.cmds.append(f'pyenv exec pip install -r {self.args.set_new_env[1]}')
                pass


    #?#####################################################################################################################
    

    def create_project_tree(self):
        if settings.venv_manager == 'poetry':
            return self
        return self.__create_project_tree__non_poetry()

    def __create_project_tree__non_poetry(self):
        path = pathlib.Path(self.args.dir)
        if path / '.git' in list(path.iterdir()):
            path2 = path / '.gitignore'
            with path2.open('w') as file:
                file.write('.python-version')
        path /= self.args.name #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        path.mkdir(exist_ok=False)
        (path / '__main__.py').touch()
        (path / 'test').mkdir()
        (path / 'test' / '__init__.py').touch()
        path /= 'src'
        path.mkdir()
        (path / '__init__.py').touch()
        path /= 'main'
        path.mkdir()
        (path / '__init__.py').touch()
        (path/'main.py').touch()
        return self
    


def main():
    proj = PyProject(parse_pyproject().parse_args()).manage_version().manage_venv().create_project_tree()
    print(' && '.join(proj.cmds))


if __name__ == '__main__':
    main()
