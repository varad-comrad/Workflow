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
  local commit_hash=$(git rev-parse "$commit_reference")
  git reset --hard "$commit_hash"
}

function workon(){
	local p=$1
    # TODO: create venv if doesn't exist
	source $1/bin/activate
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

function new_function(){
    make_workflow.py $@
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
        new_function "$@"
    elif [ $1 = 'reset' ]; then
        shift
        resetter "$@"
    elif [ $1 = '-h' ]; then
        cat advanced_helper.txt
    else
        cat helper.txt 
    fi

}