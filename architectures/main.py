from diagrams import Diagram
from diagrams.aws.compute import EC2, ElasticContainerService, Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.devtools import CommandLineInterface
from diagrams.aws.integration import StepFunctions
from diagrams.aws.management import Cloudformation, Cloudwatch
from diagrams.aws.ml import Sagemaker
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.client import Users
from diagrams.onprem.registry import Jfrog
from diagrams.onprem.vcs import Github
from diagrams.programming.framework import React
from diagrams.programming.language import Csharp, Go, Python, Rust, Typescript
from diagrams.saas.chat import Slack
from diagrams.saas.logging import Datadog

# VCS
# SourceCode

## Tests
### Unit
### Integration
### E2E
### Stress
### Load
### Benchmarks

##  Makefiles
##  Dockerfiles
##  Configurations
##  IaC

## Tools
### DebugTools
### TemplatesEngine
### MonorepoManagement
### SyntheticDataGeneration
### PreCommitHooks

## CodeQuality
### Lint, Format, StaticTypeChecking

# CI/CD
## Runners
## Workflows
## Actions
## Resources

# Auth
# Secrets

# Monitoring
## Logs
## Metrics
## Traces
## Dashboards
## Alerts

# Interfaces
## APIs
## CLIs
## UIs

# ManagementTools
## IssueTracker
## FeaturesBoard
## Tasks

# Artifacts
## Remote
## Local
## Containers

# Web
## PublicRepositories
