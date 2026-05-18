# import official library that talks to AWS

import boto3

# Tell boto3 to talk to local port 4566 instead of real internet
# Use fake passwords

fake_amazon_s3 = boto3.client('s3', 
                              endpoint_url='http://localhost:4566',
                              region_name='us-east-1',
                              aws_access_key_id='test',
                              aws_secret_access_key='test')

# Test 1: create a bucket in AWS

fake_amazon_s3.create_bucket(Bucket='my-first-bucket')
print("Success! We created a fake cloud folder!")

# Tell Boto3 to talk to 'dynamodb' service instead of 's3'

