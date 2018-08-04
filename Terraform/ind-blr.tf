## Ssh key finger print
## ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub | awk '{print $2}'

provider "digitalocean" {
token = "73b51057476b8e02388b8371085de16fbb8f09670267b4b8d3545a5200d98528"
}


resource "digitalocean_droplet" "web1" {
image = "ubuntu-18-04-x64"
name = "mywebserver01"
region = "blr1"
size = "1gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

resource "digitalocean_droplet" "web2" {
image = "fedora-28-x64"
name = "mywebserver02"
region = "blr1"
size = "1gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

resource "digitalocean_droplet" "web3" {
image = "centos-7-x64"
name = "mywebserver03"
region = "blr1"
size = "1gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

output "Public_ip" {
  value = "${digitalocean_droplet.web1.ipv4_address}"
  value = "${digitalocean_droplet.web2.ipv4_address}"
  value = "${digitalocean_droplet.web3.ipv4_address}"
}

output "Name_VM" {
  value = "${digitalocean_droplet.web1.name}"
  value = "${digitalocean_droplet.web2.name}"
  value = "${digitalocean_droplet.web3.name}"
}
