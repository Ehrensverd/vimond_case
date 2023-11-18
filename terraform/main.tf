provider "aws" {
  region  = "eu-central-1" 
}


resource "aws_iam_role" "eb_role" {
  name = "eb-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
      },
    ],
  })
}

resource "aws_iam_role_policy_attachment" "eb_web_tier" {
  role       = aws_iam_role.eb_role.name
  policy_arn = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier"
}


resource "aws_iam_instance_profile" "eb_instance_profile" {
  name = "eb-instance-profile"
  role = aws_iam_role.eb_role.name
}


resource "aws_elastic_beanstalk_application" "vimond_case" {
  name        = "vimond_api"  
  description = "My Elastic Beanstalk Application"
}

resource "aws_elastic_beanstalk_environment" "test" {
  name                = "Vimond-test" 
  application         = aws_elastic_beanstalk_application.vimond_case.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.0.6 running Python 3.9"

setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = aws_iam_instance_profile.eb_instance_profile.name
  }
}
