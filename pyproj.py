import argparse, subprocess, pathlib, settings, sys


def parse_pyproject():
    parser = argparse.ArgumentParser()
    # requires pyenv to manage python versions
    parser.add_argument('-p', '--python-version', type=str, required=True)

    parser.add_argument('-f', '--force-install',
                        default=False, action='store_true')
    # force installation of python version if not present.
    # like previous, requires pyenv.

    parser.add_argument('-e', '--env', type=str)
    # path to env.

    parser.add_argument('-s', '--set-new-env', nargs='+', default=False)

    parser.add_argument('-d', '--dir', default='.', type=str)
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
        self.args = parsed_args
        self.cmds: list[str]


    #############################################################################


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
        return self

    def __install_version_pyenv(self):
        subprocess.run(
            f'pyenv install {self.args.python_version}', shell=True, cwd=self.args.dir)
    
    def __manage_version_conda(self):
        subprocess.run(f'conda create python={self.args.python_version} -n {self.args.set_new_env[0]}', shell=True)
        return self
    

    #############################################################################

    
    def manage_venv(self):
        if settings.venv_manager == 'conda':
            ...
            return self
        else:
            if self.args.env:
                self.__choose_preexisting_venv()
            if self.args.set_new_env:
                self.__new_venv()
            return self

    def __choose_preexisting_venv(self):
        match settings.venv_manager:
            case 'virtualenv':
                #! ############################
                pass
            case 'conda':
                #! ############################
                pass
            case 'poetry':
                #! ############################
                pass

    def __new_venv(self):
        match settings.venv_manager:
            case 'virtualenv':
                subprocess.run(
                    f"virtualenv --python=python{self.args.python_version} '{self.args.set_new_env[0]}'", cwd=self.args.dir, shell=True)
            case 'poetry':
                #! ############################
                pass
        try:
            path = pathlib.Path(f'./{self.args.set_new_env[1]}')
        except IndexError:
            if self.args.data_science:
                self.__install_ds_packages()
            if self.args.web_dev:
                self.__install_wd_packages()

        if path.exists():
            self.__package_install()

    def __package_install(self):
        match settings.venv_manager:
            case 'virtualenv':
                subprocess.run(
                    f'{self.args.set_new_env[0]}/bin/python -m pip install -r {self.args.set_new_env[1]}', cwd=self.args.dir, shell=True)
            case 'conda':
                #! ############################
                pass
            case 'poetry':
                #! ############################
                pass


    def __install_ds_packages(self):
        #! ############################
        pass

    def __install_wd_packages(self):
        #! ############################
        pass




def main():
    # proj = PyProject(parse_pyproject()).manage_version().manage_venv()
    # print(proj.return_code)
    # proj = PyProject(parse_pyproject().parse_args()).choose_venv()
    print(settings.venv_manager)


if __name__ == '__main__':
    main()
