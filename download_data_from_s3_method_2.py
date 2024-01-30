import boto3
from urllib.parse import urlparse, unquote_plus
from config import Config
import os

constant = Config()

current_working_directory = os.getcwd()
s3 = boto3.client(
    's3',
    aws_access_key_id=constant.aws_access_key_id,
    aws_secret_access_key=constant.aws_secret_access_key
)

def parse_s3_uri(s3_uri):
    parsed_uri = urlparse(s3_uri)
    bucket = parsed_uri.netloc
    key = unquote_plus(parsed_uri.path.lstrip('/'))
    return bucket, key

def download_s3_object(bucket, key, filename):
    local_path = os.path.join(current_working_directory, filename)
    try:
        s3.download_file(bucket, key, local_path)
        print("Successfully downloaded the file:", local_path)
    except Exception as e:
        print("An error occurred while downloading the file:", e)
        local_path = None
    return local_path

s3_uri = "s3://test/dictionary_2pg.pdf"

bucket, key = parse_s3_uri(s3_uri)
pdf_download_path = download_s3_object(bucket, key, "input.pdf")
