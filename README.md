# RedditDE
This project is based on Reddit Data Pipeline Engineering (https://github.com/airscholar/RedditDataEngineering.git) by Yusuf Ganiyu.
I use this project as learning material and to gain deeper knowledge in data engineering.

The pipeline is designed to:

Extract data from Reddit using its API.
Store the raw data into an S3 bucket via Apache Airflow.
Transform the data using AWS Glue and Amazon Athena.
Load the transformed data into Amazon Redshift for analytics and querying.

**Architecture**
![Pipeline jpg](https://github.com/user-attachments/assets/5427b2db-755b-4b2d-b9ae-8a168d411e08)

Reddit API: Source of the data.
Apache Airflow & Celery: Orchestrate the ETL process and manage task distribution.
PostgreSQL: Temporary storage and metadata management.
Amazon S3: Raw data storage.
AWS Glue: Data cataloging and ETL jobs.
Amazon Athena: SQL-based data transformation.
Amazon Redshift: Data warehousing and analytics.

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

- Replace "your-bucket-name" with the name of your S3 bucket.
- Replace "your-file-name" with the name of your input CSV file.
- Replace "source_dynamic_frame" with source S3 and "target_dynamic_frame" with Destination S3.

