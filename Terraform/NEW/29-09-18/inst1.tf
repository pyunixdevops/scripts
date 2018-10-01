resource "digitalocean_droplet" "AnsServer-ubun-18" {
image = "ubuntu-18-04-x64"
name = "AnsServer-ubun-18"
region = "blr1"
ssh_keys = ["3f:d6:e7:08:60:63:c3:6b:d9:2d:35:23:d7:92:82:e2"]
size = "2gb"
}
