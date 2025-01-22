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
AmazonS3_node1737572688626 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://pthk-nikesh-reddit/raw/reddit_20250122.csv"], "recurse": True},
    transformation_ctx="AmazonS3_node1737572688626"
)

# Convert DynamicFrame to DataFrame
df = AmazonS3_node1737572688626.toDF()

# Clean and standardize column names
cleaned_columns = [col.strip().replace(' ', '_').replace('.', '').lower() for col in df.columns]
df = df.toDF(*cleaned_columns)

# Debugging: Print cleaned column names
print("Cleaned Column Names:", df.columns)

# Convert back to DynamicFrame
cleaned_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "cleaned_dynamic_frame")

# Write the cleaned data back to S3
AmazonS3_node1737572692987 = glueContext.write_dynamic_frame.from_options(
    frame=cleaned_dynamic_frame,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://pthk-nikesh-reddit/transformed/", "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1737572692987"
)

# Commit the job
job.commit()