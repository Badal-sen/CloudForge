output "vpc_id" {
  value = aws_vpc.cloudforge_vpc.id
}

output "public_subnet_id" {
  value = aws_subnet.public_subnet.id
}

output "internet_gateway_id" {
  value = aws_internet_gateway.igw.id
}

output "instance_id" {
  value = aws_instance.cloudforge_server.id
}

output "public_ip" {
  value = aws_instance.cloudforge_server.public_ip
}

output "public_dns" {
  value = aws_instance.cloudforge_server.public_dns
}