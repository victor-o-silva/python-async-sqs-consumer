import json
from datetime import datetime

import boto3

from _envs_values import AWS_CONNECTION_PARAMS


def _send_message(*, queue_name: str):
    sqs_resource = boto3.resource('sqs', **AWS_CONNECTION_PARAMS)
    sqs_client = boto3.client('sqs', **AWS_CONNECTION_PARAMS)
    queue = sqs_resource.get_queue_by_name(QueueName=queue_name)
    for i in range(10):
        now_str = datetime.utcnow().isoformat()
        message_body = json.dumps({"timestamp": now_str})
        sqs_client.send_message(
            QueueUrl=queue.url,
            MessageBody=message_body,
        )
        print(f"Sent message to queue {queue_name!r}. Message content: {message_body!r}")
