#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Please pass the OS type - ubuntu/centos"
    exit 1
fi

os=$1


if [ $os = "centos" ]; then

    wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    rpm -ivh epel-release-latest-7.noarch.rpm
    yum -y install epel-release
    yum -y install ansible python python-pip

elif [ $os = "ubuntu" ]; then
    apt -y update
    apt -y upgrade
    apt -y install software-properties-common
    apt-add-repository ppa:ansible/ansible
    apt -y update
    apt -y install ansible
fi

ansible --version
