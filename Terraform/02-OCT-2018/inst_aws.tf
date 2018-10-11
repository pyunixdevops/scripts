resource "aws_instance" "devopscl01" {
ami = "ami-5b673c34"
instance_type = "t2.micro"
key_name = "mac-key"
}

resource "aws_instance" "devopscl02" {
ami = "ami-5b673c34"
instance_type = "t2.micro"
key_name = "mac-key"
}

