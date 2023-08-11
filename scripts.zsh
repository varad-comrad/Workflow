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

function pythonproj(){
    python pythonproj.py $@
    workon tes
}

function mkproj(){

}

function javaproj(){

}

function mkdb(){
    python mkdb.py $@
}

function push_git(){
	python push_git.py $@
}

function mkdirproj(){

}

function workflow(){
    if [$1 = 'config']; then
        shift
        python config.py $@ 
    elif [$1 = 'mkdir']; then
        shift
        mkdirproj $@ 
    elif [$1 = 'python-project']; then
        shift
        pythonproj $@ 
    
    fi

}
