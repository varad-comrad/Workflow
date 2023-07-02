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

function pyproject(){
	cd $1
	virtualenv $2
	source $2/bin/activate
}

function reset_commit() {
  local commit_number=${1:-"1"}
  local commit_reference="HEAD~$commit_number"
  local commit_hash=$(git rev-parse "$commit_reference")
  git reset --hard "$commit_hash"
}


function new_vscode_project(){
  local directory_name=$1
  local directory_home=$2
  cd ~
  cd $directory_home
  mkdir $directory_name
  cd $directory_name
  code .
}
