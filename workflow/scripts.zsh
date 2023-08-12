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

function reset_commit() {
  local commit_number=${1:-"1"}
  local commit_reference="HEAD~$commit_number"
  local commit_hash=$(git rev-parse "$commit_reference")
  git reset --hard "$commit_hash"
}

function workon(){
	local p=$1
	source $1/bin/activate
}

function activate_venv(){
	if [ $1 = 'virtualenv' ]; then
		shift
		workon $@
	elif [ $1 = 'conda' ]; then
		shift
		conda activate $@
	elif [ $1 = 'poetry' ]; then
		shift
	fi
}

function pythonproj(){
	msg=$(pyproj.py $@)
	echo $msg
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

function workflow(){
    if [ $1 = 'config' ]; then
        shift
        python config.py "$@" 
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
    

    fi

}
