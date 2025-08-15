terraform {
  backend "s3" {
    bucket = "aws-bucket-2804"
    region = "eu-north-1"
    key    = "alex-docker/terraform.tfstate"
  }
}