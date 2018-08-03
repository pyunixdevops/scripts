
## Ssh key finger print
## ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub | awk '{print $2}'

provider "digitalocean" {
token = "73b51057476b8e02388b8371085de16fbb8f09670267b4b8d3545a5200d98528"
}

resource "digitalocean_droplet" "web4" {
image = "ubuntu-14-04-x64"
name = "mywebserver01"
region = "blr1"
size = "1gb"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
}

output "Public_ip" {
  value = "${digitalocean_droplet.web4.ipv4_address}"
}

output "Name_VM" {
  value = "${digitalocean_droplet.web4.name}"
}
