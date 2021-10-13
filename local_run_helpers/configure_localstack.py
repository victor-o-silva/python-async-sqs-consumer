import os

import boto3

from _envs_values import AWS_CONNECTION_PARAMS, SQS_QUEUE_NAME_A, SQS_QUEUE_NAME_B

CUSTOM_AWS_ENDPOINT = os.getenv("CUSTOM_AWS_ENDPOINT")
if not CUSTOM_AWS_ENDPOINT:
    print("Not using a custom AWS endpoint url. Exiting.")
    exit(1)


def main():
    sqs_resource = boto3.resource('sqs', **AWS_CONNECTION_PARAMS)

    queue_a = sqs_resource.create_queue(QueueName=SQS_QUEUE_NAME_A)
    print(f"Created queue successfully. URL: {queue_a.url!r}")

    queue_b = sqs_resource.create_queue(QueueName=SQS_QUEUE_NAME_B)
    print(f"Created queue successfully. URL: {queue_b.url!r}")

    print("\n" + "=" * 40)
    print("\nAll queues:")
    for queue in sqs_resource.queues.all():
        print(queue)


if __name__ == "__main__":
    main()
