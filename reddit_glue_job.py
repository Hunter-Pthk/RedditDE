import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

# Get the job name from arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load data from Amazon S3
source_dynamic_frame = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://<your-bucket-name>/raw/<your-file-name>.csv"], "recurse": True},
    transformation_ctx="source_dynamic_frame"
)

# Convert DynamicFrame to DataFrame
df = source_dynamic_frame.toDF()

# Clean and standardize column names
cleaned_columns = [col.strip().replace(' ', '_').replace('.', '').lower() for col in df.columns]
df = df.toDF(*cleaned_columns)

# Debugging: Print cleaned column names
print("Cleaned Column Names:", df.columns)

# Convert back to DynamicFrame
cleaned_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "cleaned_dynamic_frame")

# Write the cleaned data back to S3
glueContext.write_dynamic_frame.from_options(
    frame=cleaned_dynamic_frame,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://<your-bucket-name>/transformed/", "partitionKeys": [],
    },
    transformation_ctx="target_dynamic_frame"
)

# Commit the job
job.commit()
