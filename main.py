import requests
import json
import yaml
import logging
from pathlib import Path
import time
import boto3
from datetime import datetime

# Load config
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

api_url = config['api_url']
log_file = config['log_file']
s3_bucket = config['s3_bucket']
s3_folder = config.get('s3_folder', '')

# Setup logging (still goes to fixed log file)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='a'
)

while True:
    try:
        print("Fetching data from API...")

        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Log API success
        logging.info(f'API call successful: {api_url}')
        logging.info(f'API response: {data}')

        # Generate timestamped filenames
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        json_filename = f"output_{timestamp}.json"
        yaml_filename = f"output_{timestamp}.yaml"
        log_filename_to_upload = f"log_{timestamp}.log"

        # Save API data to JSON and YAML
        with open(json_filename, 'w') as jf:
            json.dump(data, jf, indent=4)

        with open(yaml_filename, 'w') as yf:
            yaml.dump(data, yf)

        print("API data saved to JSON and YAML.\n")

        # Upload to S3
        s3 = boto3.client("s3")

        s3.upload_file(json_filename, s3_bucket, s3_folder + json_filename)
        s3.upload_file(yaml_filename, s3_bucket, s3_folder + yaml_filename)

        # Also upload the current log file, with timestamped name
        s3.upload_file(log_file, s3_bucket, s3_folder + log_filename_to_upload)

        logging.info(f"Uploaded {json_filename}, {yaml_filename}, and log file to S3.")
        print("Uploaded all files to S3.\n")

    except Exception as e:
        logging.error(f'API or S3 operation failed: {e}')
        print("Error occurred during API call or S3 upload.\n")

    # Wait before the next run
    print("Waiting 30 seconds before next run...\n")
    time.sleep(30)
