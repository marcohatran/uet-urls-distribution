import json

import redis
import time

from controller.url_controller import update_status
from helper.datetime_helper import datetime_converter

HOST = 'localhost'
PORT = '6379'
PASS = 'UETDistribute!@#2019'
CHANNEL = 'QUEUE_LAYER_2'

r = redis.Redis(host=HOST, port=PORT, password=PASS)


def push_queue_layer_2(url_obj):
    url_obj.update({
        'status': 'added_queue_2',
        'status_id': 2,
    })
    update_status(url_obj)
    # print(url_obj)
    url_obj_message = json.dumps(url_obj, default=datetime_converter)
    pub = r.publish(
        channel=CHANNEL,
        message=url_obj_message
    )

    time.sleep(5)
