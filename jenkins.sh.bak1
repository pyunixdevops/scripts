#!/bin/sh

########################################
### Variables section ###
########################################



########################################
### Functions required for installing
### and configuring Jenkins
########################################

install()
{
	instype="$1"
	osver="$2"
	if [ $instype = "war" ]; then
		echo "Running WAR based installation with Tomcat"
		inst_war $osver
	elif [ $instype = "native" ]; then
		echo "Running native package installation"
		inst_native $osver
	else
		echo "Installation not supported"
		exit
	fi
}

inst_war()
{
	osver=$1
	if [ grep -i "cent" $osver ]; then

		rel_ver="`cat /etc/redhat-release`"
		echo "Running WAR based installation on $rel_ver"
		yum -y install java-1.8.0-openjdk wget
		rpm -qa |grep -i "java-1.8"
		if [ $? -eq 0 ]; then
			echo "Java 1.8 is installed"
		else
			echo "Java installation failed"
		fi
	fi

}


