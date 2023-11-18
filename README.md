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
