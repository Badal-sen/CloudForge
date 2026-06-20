#!/bin/bash

dnf update -y

dnf install docker git -y

systemctl enable docker
systemctl start docker

usermod -aG docker ec2-user