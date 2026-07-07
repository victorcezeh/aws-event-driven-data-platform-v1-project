# aws-event-driven-data-platform 🏗️

> 🚧 In progress - built alongside AWS SAA exam prep 😁

## Context

This project started as a way to make my AWS SAA studying concrete. Instead of just reading about S3, VPC, IAM, and CloudFormation, I wanted to actually build something with them. Something that resembles a real production data platform.

The result is an event-driven pipeline that ingests raw JSON from an external API, processes it with AWS Lambda inside a private VPC, and loads the results into a Redshift Serverless data warehouse. Fully provisioned with CloudFormation and deployed via GitHub Actions CI/CD.

## Infrastructure 🔧

Each stack is purpose-built and independently deployable via `main_stack.yaml`.

| Stack | What it does |
|-------|-------------|
| `vpc.yaml` | 🌐 Private VPC, subnets, route tables, VPC endpoints |
| `iam_role.yaml` | 🔐 Least-privilege IAM roles for Lambda and Redshift |
| `s3.yaml` | 🪣 S3 bucket with versioning, HTTPS enforcement, event trigger |
| `secrets_manager.yaml` | 🔑 Auto-generated Redshift credentials |
| `lambda.yaml` | ⚡ Python 3.14 Lambda inside private VPC |
| `redshift.yaml` | 🏭 Redshift Serverless in private subnet |
| `monitoring.yaml` | 📊 CloudWatch alarms, log groups, SNS email alerts |
| `main_stack.yaml` | 🎯 Nested stack orchestrator |


## Project Structure

\```
aws-event-driven-data-platform-v1-project/
├── .github/
│   └── workflows/
│       └── ci.yaml
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logging_config.py
├── data/
│   ├── processed/
│   │   └── .gitkeep
│   └── raw/
│       └── .gitkeep
├── docs/
│   └── ARCHITECTURE.md
├── infrastructure/
│   ├── iam_role.yaml
│   ├── lambda.yaml
│   ├── main_stack.yaml
│   ├── monitoring.yaml
│   ├── redshift.yaml
│   ├── s3.yaml
│   ├── secrets_manager.yaml
│   └── vpc.yaml
├── lambda/
│   └── handler.py
├── logs/
│   └── pipeline.log
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── load_redshift.py
│   ├── load_s3.py
│   ├── s3_event_reader.py
│   └── transform.py
├── tests/
│   ├── test_extract.py
│   ├── test_load_s3.py
│   └── test_transform.py
├── .env.example
├── .gitignore
├── LICENSE
├── pipeline.py
├── README.md
└── requirements.txt
\```

More Ideas to add to the documentation:
- Problem: What problem does the platform solve?
- Architecture: Why is each component there?
- Implementation: Show the code and infrastructure.
- Trade-offs: Explain why these choices were made.
- Future improvements: Show awareness of what could be better either on this project or another
- Show debugging stories and failures in the repo.