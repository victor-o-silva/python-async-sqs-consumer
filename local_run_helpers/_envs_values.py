import os

CUSTOM_AWS_ENDPOINT = os.getenv("CUSTOM_AWS_ENDPOINT")  # If using localstack https://github.com/localstack/localstack
SQS_QUEUE_NAME_A = os.getenv("SQS_QUEUE_NAME_A")
SQS_QUEUE_NAME_B = os.getenv("SQS_QUEUE_NAME_B")

if CUSTOM_AWS_ENDPOINT:
    AWS_CONNECTION_PARAMS = {
        "endpoint_url": CUSTOM_AWS_ENDPOINT,
        "aws_access_key_id": "-",
        "aws_secret_access_key": "-",
        "aws_session_token": "-",
    }
else:
    AWS_CONNECTION_PARAMS = {}

