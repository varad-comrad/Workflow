alias zshrc="open ~/.zshrc"
alias anaconda="conda run anaconda-navigator" 

function pgadm(){
	cd ...
	source ../bin/activate
	pgadmin4 &
	sleep 5
	xdg-open http://127.0.0.1:5050
	gnome-terminal
}

function lvpgam(){
	pid_pgadmin=$(pgrep pgadmin)
	
	deactivate
	cd -
}

function resetter(){
    if [ $1 = 'commit' ]; then
        shift
        reset_commit $@
    fi 
}

function reset_commit() {
  local commit_number=${1:-"1"}
  local commit_reference="HEAD~$commit_number"
  git reset --hard "$commit_reference"
}

function workon(){
	local p=$(workon.py $@)
	eval $p
}

function pythonproj(){
	msg=$(pyproj.py $@)
    vman=$(echo $msg | tail -n 1)
    eval $vman
}

function mkproj(){
	mkproj.py $@
}

function javaproj(){
	javaproj.py $@
}

function mkdb(){
    mkdb.py $@
}

function push_git(){
	push_git.py $@
}

function mkdirproj(){
	mkdirproj.py $@
}

function activate_shell(){
    shell.py 
}

function runner(){
    coderunner.py "$@"
}

function runmanager(){
    if [ $1 = 'download' ]; then
        shift
        downloadmanager.py "$@"        
    else
        echo "ERROR: Unexpected argument '$1'. Options are ..."  
    fi
}

function new_workflow(){
    if [ $1 = 'function' ]; then
        shift
        make_workflow.py "$@"
    elif [ $1 = 'alias' ]; then
        shift
        alias.py "$@"        
    elif [ $1 = 'download-pattern' ]; then
        shift
        configdownload.py "$@"        
    else
        echo "ERROR: Unexpected argument '$1'. Options are 'function', 'alias'"  
    fi
}

function workflow_docker(){
    if [ $1 = 'new' ]; then
        shift
        new_docker "$@"
    elif [ $1 = 'use' ]; then
        shift
        use_docker "$@"
    fi
}

function workflow(){

    if [ $# -eq 0 ]; then
        activate_shell
    elif [ $1 = 'config' ]; then
        shift
        config.py "$@" 
    elif [ $1 = 'mkdir' ]; then
        shift
        mkdirproj "$@" 
    elif [ $1 = 'pythonproj' ]; then
        shift
        pythonproj "$@" 
    elif  [ $1 = 'mkdb' ]; then
        shift
        mkdb "$@" 
    elif  [ $1 = 'push' ]; then
        shift
        push_git "$@" 
    elif [ $1 = 'new' ]; then
        shift
        new_workflow "$@" 
    elif [ $1 = 'reset' ]; then
        shift
        resetter "$@"
    elif [ $1 = 'run' ]; then
        shift 
        runner "$@" 
    elif [ $1 = 'docker' ]; then
        shift 
        workflow_docker "$@" 
    elif [ $1 = 'manager' ]; then
        shift 
        runmanager "$@" 
    elif [ $1 = '-h' ]; then
        cat text_files/advanced_helper.txt
    else
        cat text_files/helper.txt 
    fi

}

function loc() {
    if [ $# -eq  0 ]; then
        git ls-files | xargs wc -l
    else
        git ls-files | grep $1 | xargs wc -l
    fi
}

