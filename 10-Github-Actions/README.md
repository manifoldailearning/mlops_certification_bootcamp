# GitHub Actions MLOps Demo

This repository demonstrates a CI/CD pipeline using GitHub Actions to automatically build and push Docker images to Docker Hub.

## Workflow Overview

The repository contains a GitHub Actions workflow that automatically builds and pushes Docker images to Docker Hub whenever changes are pushed to the `main` branch.

### Workflow File Location
The workflow is defined in `.github/workflows/docker-build-push.yml`

## Workflow Steps

1. **Trigger**
   - The workflow is triggered on every push to the `main` branch

2. **Environment**
   - Runs on `ubuntu-latest` runner

3. **Steps**
   - **Checkout Source**: Clones the repository code
   - **Get Commit Hash**: Captures the current commit SHA for versioning
   - **Build Docker Image**: Builds the Docker image with two tags:
     - Latest commit hash
     - `latest` tag
   - **Push Docker Image**: Pushes both tagged images to Docker Hub

## Required Secrets

To use this workflow, you need to set up the following secrets in your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

## How to Set Up Secrets

1. Go to your GitHub repository
2. Navigate to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Add the required secrets mentioned above

## Docker Image Tags

The workflow creates two tags for each build:
- `latest`: Always points to the most recent build
- `{commit-hash}`: Points to a specific build based on the commit SHA

## Usage

1. Push your code to the `main` branch
2. The workflow will automatically:
   - Build your Docker image
   - Tag it with the commit hash and 'latest'
   - Push it to Docker Hub

## Security Notes

- Never commit sensitive information like passwords or tokens directly in the workflow files
- Use GitHub Secrets for storing sensitive credentials
- Consider using Docker Hub access tokens instead of your main password
