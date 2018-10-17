#!/bin/sh

# Shebang line - It gets executed when you call the script.
# Hash is for comment. where as ! for negate or not-equal.
# So, you are saying don't consider this as a comment.
# Execute the first line. It should be an executable and it should be in 1st line.

# Please change this link
github_link="git@github.com:pyunixdevops/devops_ci.git"

#Do not change this link
devops_git="git@github.com:pyunixdevops/devops_ci.git"

repo_name="devops_ci"
home_dir='/Users/sankartest/export'

clone_repo()
{
    if [ $# -ne 1 ]; then
        echo "Please pass repo_name as \$1"
        return
    fi

    if [ -d $home_dir/$repo_name ]; then
        echo "Directory $home_dir/$repo_name already exists"
        echo "Go ahead and pull the repo $home_dir/$repo_name"
        cd $home_dir/$repo_name
        git pull
    else
        echo "Directory $home_dir/$repo_name doesn't exists"
        echo "Go ahead and clone the repo $home_dir/$repo_name"
        cd $home_dir
        git clone $github_link
    fi
}

copy_files()
{
    echo "Copying all files required for devops_ci git repo"
    cd $home_dir/test_repo
    git clone $devops_git
    cd $repo_name ; cp -r Ansible Python Shell Terraform $home_dir/$repo_name
    cd $home_dir
    rm -rf $home_dir/test_repo
}


push_changes()
{
    repo_name="$1"
    message="$2"
    if [ $# -ne 2 ]; then
        echo "Please pass repo_name as \$1 and the message as \$2"
        return
    fi

    if [ -d $home_dir/$repo_name ]; then
        cd $home_dir/$repo_name
        git add . ; git commit -m "$message"
        git push -u origin master
        cd $home_dir
    else
        echo "The repo $home_dir/$repo_name is not available"
    fi
}

deploy()
{
    repo_name="$1"
    echo "Setup the environment using Terraform and deploy using Ansible"
    cd $home_dir/$repo_name/Shell
    ./deploy.sh
}

check()
{
    repo_name="$1"
    echo "Check CI Status..."
    cd $home_dir/$repo_name/Shell
    ./check.sh
}

remove()
{
    echo "Destroy the setup..."
    cd $home_dir/$repo_name/Shell
    ./remove.sh
}

update()
{
    echo "Destroy the setup..."
    cd $home_dir/$repo_name/Shell
    ./update.sh
}

#push_changes
#clone_repo
#push_changes $home_dir/$repo_name "My new commit for DevOps Ansible"

create_setup()
{
clone_repo $repo_name
copy_files
push_changes $repo_name "All required config files for AWS, Terraform and Ansible"
deploy $repo_name
}

create_setup






