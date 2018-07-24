#!/bin/sh

op=$1

if [ $os = "centos" ]; then

    yum -y install epel-release
    yum -y install ansible

elif [ $os = "ubuntu" ]; then
    apt -y update
    apt -y upgrade
    apt -y install software-properties-common

    apt-add-repository ppa:ansible/ansible

    apt -y update

    apt -y install ansible
fi

ansible --version
