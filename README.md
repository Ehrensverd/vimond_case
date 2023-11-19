# Overview

This project involves developing a program that processes two sets of intervals ('include' and 'exclude') and outputs the result as sorted, non-overlapping intervals with integer values. The input may be unordered, overlapping, or empty. 

## Solution
I will split the task into to parts: DevOps and Development.

# DevOps 

### Environment Setup

- **Terraform Script**: A Terraform script is used to create two AWS environments: a test environment and a production environment. These environments leverage AWS services such as IAM, Elastic Beanstalk, and RDS.
- **Local Development Environment**: A third environment is set up locally on my laptop for development purposes.

### CI/CD Pipeline

- **GitHub Actions**: A CI/CD pipeline is established using GitHub Actions. This pipeline automates the deployment and testing of code pushed to the GitHub repository.
- **Test Environment Integration**: Any commit or pull request will trigger testing in the test environment.
- **Main Branch Protection**: Merging into the main branch is restricted if any tests fail.

### Cost Control

- To avoid unintended costs in AWS, the runtime and usage of cloud environments are limited. Most of the runtime and stress testing are conducted in the local environment.

# Development Component

### API Development

- **Framework**: A simple Django API is set up to create the necessary endpoints.
- **Input Variability**: Given the task requirements, the inputs to the endpoint could vary significantly. There might be large ranges or a high number of sets in the given data.

### Algorithm Selection and Optimization

- **Initial Setup**: The first step involves setting up endpoint tests and selecting a preliminary algorithm based on research. This algorithm doesn't need to be optimal at this stage.
- **Metric Testing**: We will set up metric testing for different algorithms to determine which performs better under various types of input. This involves creating random set generators and automated testing, along with performance timing.
- **Performance Optimization**: The second part of the development focuses on optimizing performance, possibly through caching and input sorting.

# Project Summary

## PRs
Feat: Terraform Script for AWS Environment Setup https://github.com/Ehrensverd/vimond_case/pull/1

Feat: Django Server Setup https://github.com/Ehrensverd/vimond_case/pull/2

Fix: handle negative input intervals; add testshttps://github.com/Ehrensverd/vimond_case/pull/3

Feat: Implement GitHub Actions CI/CD for Django Server https://github.com/Ehrensverd/vimond_case/pull/4

### Github screenpaste access broke
After I made the repo public, I noticed my screenshots in the pull requests had all broken.
So I reuploaded them all into one issue, as I did not have time to put them back in the PRs

## Completed Work
- **Terraform Script Setup:** Configured Elastic Beanstalk for both test and production environments using Terraform scripts.
- **AWS Prod Environment:** The production environment in AWS was terminated to minimize billing.
- **Django Server Setup:** Implemented a basic setup for a bare-bones Django server.
- **Testing and Bug Fixing:** Wrote necessary tests and implemented a solution. Addressed a bug related to handling negative integers in set intervals.
- **CI/CD with GitHub Actions:** Initiated continuous integration and deployment using GitHub Actions, focusing mainly on the test environment.
 - More about issues I had with this can be read here: https://github.com/Ehrensverd/vimond_case/issues/5 
- **API Testing Files:** Created `test_endpoint.ps1` for local API testing and `test_endpoint_aws.ps1` for testing on the AWS web server.

## Future Development
- **Algorithm Optimization:** Due to time constraints, the planned optimization for selecting algorithms based on input variations was not completed. The goal is to create a script to test different input types, record processing times, and dynamically select algorithms for performance optimization.
- **GitHub Actions for Prod Environment:** Deployment to the production environment using GitHub Actions was not set up and remains a future task.

## Additional Notes
- The test environment is currently operational, and all GitHub action tests are passing.
- Further improvements and optimizations are planned for subsequent phases of the project.


## Terraform Setup for Elastic Beanstalk
This project uses a Terraform script to set up Elastic Beanstalk environments for testing and production purposes.

## Setup Instructions
#### Windows
1. Download and install Terraform from [Terraform.io](https://www.terraform.io/downloads.html).
2. Clone the repository: `git clone https://github.com/Ehrensverd/vimond_case`.
3. Navigate to the Terraform script directory: `cd path/to/terraform-script`.
4. Initialize Terraform: `terraform init`.
5. Apply the Terraform script: `terraform apply`.

#### Linux
1. Install Terraform using your package manager or download from [Terraform.io](https://www.terraform.io/downloads.html).
2. Clone the repository: `git clone https://github.com/Ehrensverd/vimond_case`.
3. Navigate to the Terraform script directory: `cd path/to/terraform-script`.
4. Initialize Terraform: `terraform init`.
5. Apply the Terraform script: `terraform apply`.

## Django Server Setup
A basic Django server setup is included. Follow these instructions to get it up and running.


#### Windows
1. Clone the repository: `git clone https://github.com/Ehrensverd/vimond_case`.
2. Navigate to the Django project directory: `cd path/to/vimond_server`.
3. Create a virtual environment: `python -m venv venv`.
4. Activate the virtual environment: `.\venv\Scripts\activate`.
5. Install dependencies: `pip install -r requirements.txt`.
6. Run the Django server: `python manage.py runserver`.

#### Linux
1. Clone the repository: `git clone https://github.com/Ehrensverd/vimond_case`.
2. Navigate to the Django project directory: `cd path/to/vimond_server`.
3. Create a virtual environment: `python3 -m venv venv`.
4. Activate the virtual environment: `source venv/bin/activate`.
5. Install dependencies: `pip install -r requirements.txt`.
6. Run the Django server: `python3 manage.py runserver`.

## Testing Scripts
Two scripts are provided for testing the API:
- `test_endpoint.ps1` for local testing
- `test_endpoint_aws.ps1` for testing the AWS web server

#### API Test Input Example (Windows)
```powershell
$uri = 'http://vimond-test.eba-vndd7pnc.eu-central-1.elasticbeanstalk.com/api/process_intervals/'

$body = @{
    includes = @( @(4, 22), @(-4, -1), @(34, 76) )
    excludes = @( @(5, 10), @(35, 40) )
}

$jsonBody = $body | ConvertTo-Json -Depth 10

$headers = @{
    "Content-Type" = "application/json"
}

$response = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $jsonBody
$response.Content
```

#### API Testing with Curl

Use the following `curl` command to test the API:

```bash
curl -X POST http://vimond-test.eba-vndd7pnc.eu-central-1.elasticbeanstalk.com/api/process_intervals/ \
-H "Content-Type: application/json" \
-d '{
    "includes": [[4, 22], [-4, -1], [34, 76]],
    "excludes": [[5, 10], [35, 40]]
}'
```
