# RedditDE
This project is based on Reddit Data Pipeline Engineering (https://github.com/airscholar/RedditDataEngineering.git) by Yusuf Ganiyu.
I use this project as learning material and to gain deeper knowledge in data engineering.

**AWS Glue ETL Script for Cleaning and Transforming CSV Data**

This repository contains an AWS Glue ETL script designed to load CSV data from an Amazon S3 bucket, clean and standardize column names, and save the transformed data back to another S3 bucket. The script is written in Python and uses the AWS Glue and PySpark libraries.

**Prerequisites**

AWS Glue:
AWS Glue job with the appropriate IAM role configured.

S3 Buckets:
Ensure you have S3 buckets for the raw data (input) and transformed data (output).

Python Libraries:
AWS Glue library.

PySpark.
IAM Role Permissions:

Access to read from the source S3 bucket.
Access to write to the target S3 bucket.

- Replace <your-bucket-name> with the name of your S3 bucket.
- Replace <your-file-name> with the name of your input CSV file.
- Replace "source_dynamic_frame" with source S3 and "target_dynamic_frame" with Destination S3.
