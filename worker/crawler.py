import json
import time
import logging
import redis

from controller.queue_layer_2_controller import push_queue_layer_2
from controller.url_controller import find_urls_should_add_queue_2, update_status
from helper.datetime_helper import datetime_converter

HOST = 'localhost'
PORT = '6379'
PASS = 'UETDistribute!@#2019'
CHANNEL = 'QUEUE_LAYER_2'

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    r = redis.Redis(host=HOST, port=PORT, password=PASS)
    pub = r.pubsub()
    pub.subscribe(CHANNEL)

    while True:
        data = pub.get_message()
        if data:
            # print(data)
            message = data['data']
            if message and message != 1:
                url_obj = json.loads(message.decode('utf-8'))
                logging.info("Prepare crawl: " + json.dumps(url_obj, default=datetime_converter))
                time.sleep(2)
                logging.info("Store data: " + json.dumps(url_obj, default=datetime_converter))
                url_obj.update({
                    'status': 'crawled',
                    'status_id': 3,
                })
                update_status(url_obj)
        time.sleep(5)
