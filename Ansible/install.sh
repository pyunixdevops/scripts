#!/bin/sh

apt -y update
apt -y upgrade
apt -y install software-properties-common

apt-add-repository ppa:ansible/ansible

apt -y update

apt -y install ansible

ansible --version
