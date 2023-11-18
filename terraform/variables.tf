variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}

variable "environments" {
  description = "List of environments to create"
  type        = list(string)
  default     = ["test", "prod"]
}

variable "solution_stack_name" {
  description = "Solution stack for Elastic Beanstalk"
  type        = string
  default     = "64bit Amazon Linux 2023 v4.0.6 running Python 3.9"
}
