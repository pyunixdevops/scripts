resource "digitalocean_droplet" "AnsServer-ubun-18-02" {
image = "ubuntu-18-04-x64"
name = "AnsServer-ubun-18-02"
region = "blr1"
ssh_keys = ["6e:1f:57:b5:95:db:9a:10:b6:17:ea:d8:28:6e:88:03"]
size = "2gb"
}

resource "digitalocean_droplet" "AnsServer-ubun-18-03" {
image = "ubuntu-18-04-x64"
name = "AnsServer-ubun-18-02"
region = "blr1"
ssh_keys = ["6e:1f:57:b5:95:db:9a:10:b6:17:ea:d8:28:6e:88:03"]
size = "4gb"
}
