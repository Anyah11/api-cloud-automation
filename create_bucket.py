import os

import boto3
from botocore.exceptions import ClientError

bucket_name = "kelechi-api-logs"
region = "ca-central-1"

def create_bucket(bucket_name, region):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

        print(f"Bucket {bucket_name} created successfully")
    except ClientError as e:
        print(f"Bucket {bucket_name} creation failed: {e}")
        return False
    return True

if __name__ == '__main__':
    create_bucket(bucket_name, region)
