resource "aws_instance" "example" {
  ami = "ami-5b673c34"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.aws-mac-key.key_name}"
  security_groups = ["${aws_security_group.allow_ssh.name}"]

tags {
  Name = "inst1_deploy_aws1"
  }
}

resource "aws_instance" "example2" {
  ami = "ami-5b673c34"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.aws-mac-key.key_name}"
  security_groups = ["${aws_security_group.allow_ssh.name}"]

tags {
  Name = "inst2_deploy_aws2"
  }
}

resource "aws_instance" "example3" {
  ami = "ami-5b673c34"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.aws-mac-key.key_name}"
  security_groups = ["${aws_security_group.allow_ssh.name}"]

tags {
  Name = "inst3_deploy_aws3"
  }
}

resource "aws_instance" "example4" {
  ami = "ami-5b673c34"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.aws-mac-key.key_name}"
  security_groups = ["${aws_security_group.allow_ssh.name}"]

tags {
  Name = "inst4_deploy_aws4"
  }
}

resource "aws_key_pair" "aws-mac-key" {
  key_name   = "aws_mac_key"
  public_key = "${file("~/.ssh/id_rsa.pub")}"
}

resource "aws_security_group" "allow_ssh" {
  name = "allow_ssh"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "example_public_dns" {
  value = "${aws_instance.example-new2.*.public_dns}"
}
