![Python](https://img.shields.io/badge/python-3.10-blue)
![AWS](https://img.shields.io/badge/aws-s3%20%7C%20ses-orange)
![MIT License](https://img.shields.io/badge/license-MIT-green)
# 🌐 API Automation with Python + AWS

This project fetches live API data, saves it in JSON and YAML formats, uploads it to AWS S3 every 30 seconds.

## 🔧 Technologies Used

- Python (requests, boto3, pyyaml)
- AWS S3 (storage)
- Logging module
- Git & GitHub

## 📁 Features

✅ Fetches API data every 30 seconds  
✅ Saves as `.json` and `.yaml`  
✅ Uploads to S3 with timestamped filenames  
✅ Sends email alerts on failure (via AWS SES)  
✅ Clean, reusable config (`config.yaml`)  

## 🛠 Setup

```bash
https://github.com/kelechianyanwu/api-cloud-automation
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
