import uuid
import logging


def create_uuid():
    generated_uuid = uuid.uuid1()
    return str(generated_uuid)
