

output "vimond_case_name" {
  value = aws_elastic_beanstalk_application.vimond_case.name
}

output "eb_instance_profile_name" {
  value = aws_iam_instance_profile.eb_instance_profile.name
}
