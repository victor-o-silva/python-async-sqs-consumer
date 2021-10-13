import asyncio
import os
import traceback
from typing import Callable, Any, Awaitable

import boto3

CUSTOM_AWS_ENDPOINT = os.getenv("CUSTOM_AWS_ENDPOINT")  # If using localstack https://github.com/localstack/localstack
if CUSTOM_AWS_ENDPOINT:
    AWS_CONNECTION_PARAMS = {
        "endpoint_url": CUSTOM_AWS_ENDPOINT,
        "aws_access_key_id": "-",
        "aws_secret_access_key": "-",
        "aws_session_token": "-",
    }
else:
    AWS_CONNECTION_PARAMS = {}

SQS_QUEUE_NAME_A = os.getenv("SQS_QUEUE_NAME_A")
SQS_QUEUE_NAME_B = os.getenv("SQS_QUEUE_NAME_B")
sqs_resource = boto3.resource('sqs', **AWS_CONNECTION_PARAMS)


async def poll_queue(sqs_queue, handle_message: Callable[[Any], Awaitable[None]]):
    print(f"Started polling queue {sqs_queue!r}")
    while True:
        await asyncio.sleep(1)
        messages = sqs_queue.receive_messages(MaxNumberOfMessages=10)
        message_count = len(messages)
        if message_count:
            print("=" * 60)
            print(f"Polled {message_count} messages")

        for index, message in enumerate(messages, start=1):
            print(f"Processing message {index}/{message_count}")
            try:
                await handle_message(message)
            except Exception as ex:
                traceback.print_exc()
                print(f"Error processing message: {ex}. Handler: {handle_message.__name__!r} | Message: {message!r}")
            print("-" * 40)


async def process_message_a(sqs_message):
    print(f"process_message_a - {sqs_message.body!r}")
    sqs_message.delete()


async def process_message_b(sqs_message):
    print(f"process_message_b - {sqs_message.body!r}")
    sqs_message.delete()


async def main():
    coroutines = []
    for queue, async_handler_func in [
        (
            sqs_resource.get_queue_by_name(QueueName=SQS_QUEUE_NAME_A),
            process_message_a,
        ),
        (
            sqs_resource.get_queue_by_name(QueueName=SQS_QUEUE_NAME_B),
            process_message_b,
        ),
    ]:
        coroutines.append(
            poll_queue(sqs_queue=queue, handle_message=async_handler_func)
        )

    await asyncio.gather(*coroutines)


if __name__ == "__main__":
    asyncio.run(main())
