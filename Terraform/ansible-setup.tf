################################################################## 
## Terraform setup to access Digital ocean API access
## 1. You need API token on Digital ocean
## 2. Copy public key from your Terraform m/c to Digital ocean->Security->SSH_keys
## 3. Create API token from API section and copy it to terraform.
## Ssh key finger print
## Create API token and copy it to your Terraform
## ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub | awk '{print $2}'
################################################################## 

## Create API token and copy it to your Terraform
provider "digitalocean" {
token = "131ef6b8955717022b71a08e9312a8bf74ad070bf7c72eb28d1157c4d9ab1c60"
}

resource "digitalocean_droplet" "AnsServer-ubun-18" {
image = "ubuntu-18-04-x64"
name = "AnsServer-ubun-18"
region = "blr1"
size = "8gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

resource "digitalocean_droplet" "AnsClient-fedo-28" {
image = "fedora-28-x64"
name = "AnsClient-fedo-28"
region = "blr1"
size = "2gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

resource "digitalocean_droplet" "AnsClient-cent-07" {
image = "centos-7-x64"
name = "AnsClient-cent-07"
region = "blr1"
size = "2gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

resource "digitalocean_droplet" "AnsClient-ubun-18" {
image = "ubuntu-18-04-x64"
name = "AnsClient-ubun-18"
region = "blr1"
size = "2gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

output "Public_ip" {
  value = "${digitalocean_droplet.AnsServer-ubun-18.ipv4_address}"
}

output "Name_VM" {
  value = "${digitalocean_droplet.AnsServer-ubun-18.name}"
}
