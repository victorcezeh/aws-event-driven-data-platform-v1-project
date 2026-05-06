# aws-event-driven-data-platform

## Project Structure (prototype)

```
aws-data-pipeline-starter/
│
├── infrastructure/                  # CloudFormation stacks
│   ├── main_stack.yaml              # Root stack — orchestrates all nested stacks
│   ├── vpc.yaml                     # VPC, private/public subnets, security groups
│   ├── iam.yaml                     # Roles and permissions
│   ├── s3.yaml                      # S3 buckets and event notification config
│   ├── lambda.yaml                  # Lambda function, trigger, and VPC config
│   └── redshift.yaml                # Redshift cluster and table setup
│
├── lambdas/
│   └── process_handler.py           # Lambda entrypoint: reads S3 → transforms → loads Redshift
│
├── src/                             # Reusable modules
│   ├── __init__.py
│   ├── api_fetcher.py               # Calls the external API
│   ├── s3_writer.py                 # Writes raw JSON to S3 (runs locally)
│   ├── s3_reader.py                 # Fetches S3 object content (used by Lambda)
│   ├── transformer.py               # Transforms raw data before loading (used by Lambda)
│   ├── redshift_writer.py           # Executes COPY command into Redshift (used by Lambda)
│   ├── config.py                    # Environment variable helpers and constants
│   └── logging_config.py            # Logging setup
│
├── logs/
│   └── log_file
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```