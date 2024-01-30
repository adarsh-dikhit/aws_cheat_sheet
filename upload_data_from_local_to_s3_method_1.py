import boto3
from config import Config
import os

constant = Config()

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

object_key = 'input_1.pdf'  # The path and name you want to use in S3
local_file_path = 'input.pdf'  # The path to your local file

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=constant.aws_access_key_id,
    aws_secret_access_key=constant.aws_secret_access_key
)

# Upload the file to S3
try:
    s3_client.upload_file(local_file_path, constant.s3_bucket, object_key)
    print(f"Successfully uploaded {local_file_path} to S3 at {constant.s3_bucket}/{object_key}")
except Exception as e:
    print(f"An error occurred while uploading to S3: {e}")
