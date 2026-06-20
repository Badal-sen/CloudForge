resource "aws_key_pair" "cloudforge_key" {
  key_name   = "cloudforge-key"
  public_key = file("../keys/cloudforge-key.pub")

  tags = {
    Name = "cloudforge-key"
  }
}