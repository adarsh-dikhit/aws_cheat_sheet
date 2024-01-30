import boto3
from config import Config
import os

constant = Config()

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

object_key = 'dictionary_2pg.pdf'  # Name of the key in S3
local_file_path = 'dataset.pdf'  # Name for the downloaded file

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=constant.aws_access_key_id,
    aws_secret_access_key=constant.aws_secret_access_key
)

try:
    s3_client.download_file(constant.s3_bucket, object_key, local_file_path)
    print("Successfully downloaded the file:", local_file_path)
except Exception as e:
    print("An error occurred while downloading the file:", e)

