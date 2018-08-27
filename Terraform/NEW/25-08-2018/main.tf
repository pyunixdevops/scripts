provider "digitalocean" {
token = "$digitalocean_token"
ssh_keys = ["$ssh_key"]
}

provider "aws" {
region = "ap-south-1"
access_key = "$access_key"
secret_key= "$secret_key"
}

resource "aws_instance" "devopscl01" {
ami = "ami-5b673c34"
instance_type = "t2.micro"
}

