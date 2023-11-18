
provider "aws" {
  region = var.region
}

module "eb_common" {
  source    = "./eb_common"
  app_name  = "vimond_api"
}

resource "aws_elastic_beanstalk_environment" "eb_env" {
  count               = length(var.environments)
  name                = "Vimond-${var.environments[count.index]}"
  application         = module.eb_common.vimond_case_name
  solution_stack_name = var.solution_stack_name

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = module.eb_common.eb_instance_profile_name
  }
}