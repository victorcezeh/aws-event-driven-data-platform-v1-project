```markdown
# aws-event-driven-data-platform 🏗️

> 🚧 In progress — built alongside AWS SAA exam prep 😁

## Context

This project started as a way to make my AWS SAA studying concrete. Instead of just reading about S3, VPC, IAM, and CloudFormation, I wanted to actually build something with them — something that resembles a real production data platform.

The result is an event-driven pipeline that ingests raw JSON from an external API, processes it with AWS Lambda inside a private VPC, and loads the results into a Redshift Serverless data warehouse. Fully provisioned with CloudFormation.

## Infrastructure 🔧

Each stack is purpose-built and independently deployable via `main_stack.yaml`.

| Stack | Description |
|-------|-------------|
| `vpc.yaml` | 🌐 Private VPC, subnets across two AZs, route tables, and VPC endpoints for S3, Secrets Manager, CloudWatch, and SNS |
| `iam_role.yaml` | 🔐 Least-privilege IAM roles for Lambda and Redshift |
| `s3.yaml` | 🪣 Single bucket with raw and processed prefixes, versioning, HTTPS enforcement, and S3 event notification to trigger Lambda |
| `secrets_manager.yaml` | 🔑 Auto-generated Redshift credentials stored encrypted at rest |
| `lambda.yaml` | ⚡ Python 3.14 Lambda function with VPC config, security group, and environment variables |
| `redshift.yaml` | 🏭 Redshift Serverless namespace and workgroup with private subnet placement |
| `monitoring.yaml` | 📊 CloudWatch log groups, metric alarms, SNS topic, and email alerting |
| `main_stack.yaml` | 🎯 Nested stack orchestrator — deploys all stacks in correct dependency order |
```