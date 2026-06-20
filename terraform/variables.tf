variable "aws_region" {
  description = "AWS Region"
  type        = string
}

variable "project_name" {
  description = "Project Name"
  type        = string
}

variable "environment" {
  description = "Environment"
  type        = string
}

variable "ami_id" {
  description = "Amazon Linux 2023 AMI"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}