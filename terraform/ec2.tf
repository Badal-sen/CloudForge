resource "aws_instance" "cloudforge_server" {

  ami           = var.ami_id
  instance_type = var.instance_type

  subnet_id = aws_subnet.public_subnet.id

  vpc_security_group_ids = [
    aws_security_group.cloudforge_sg.id
  ]

  key_name = aws_key_pair.cloudforge_key.key_name

  associate_public_ip_address = true

  user_data = file("${path.module}/userdata.sh")

  tags = {
    Name        = "cloudforge-server"
    Environment = var.environment
  }
}