#!/bin/sh

# Shebang line - It gets executed when you call the script.
# Hash is for comment. where as ! for negate or not-equal.
# So, you are saying don't consider this as a comment.
# Execute the first line. It should be an executable and it should be in 1st line.

github_link="git@github.com:pyunixdevops/devops_ci.git"
repo_name="devops_ci"
#work_dir="~/devops"

clone_repo()
{
    if [ -d $repo_name ]; then
        echo "Directory $repo_name already exists"
        echo "Go ahead and pull the repo $repo_name"
        cd $repo_name
        git pull $github_link/$repo_name
    else
        echo "Directory $repo_name doesn't exists"
        echo "Go ahead and clone the repo $repo_name"
        git clone $github_link/$repo_name
    fi
}

push_changes()
{
    message="$1"
    if [ $# -ne 1 ]; then
        echo "Please pass on the message as \$1"
        return
    fi
    cd $repo_name
    git add . ; git commit -m "$message"
    git push -u origin master

}

#push_changes
clone_repo
push_changes "My new commit for DevOps Ansible"



