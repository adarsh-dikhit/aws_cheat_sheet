s3_bucket = "your-bucket-name"
aws_access_key_id='your-access-key'
aws_secret_access_key='your-secret-key'
region = "us-east-1"


class Config:
    def __init__(self):
        self.s3_bucket = s3_bucket
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region = region