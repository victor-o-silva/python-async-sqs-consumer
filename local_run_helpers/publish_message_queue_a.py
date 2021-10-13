from _envs_values import SQS_QUEUE_NAME_A
from _publish_message import _send_message


if __name__ == "__main__":
    _send_message(queue_name=SQS_QUEUE_NAME_A)
