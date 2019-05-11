import time
import logging
import redis

from controller.queue_layer_2_controller import push_queue_layer_2
from controller.url_controller import find_urls_should_add_queue_2, update_status

HOST = 'localhost'
PORT = '6379'
PASS = 'UETDistribute!@#2019'
CHANNEL = 'QUEUE_LAYER_1'

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    r = redis.Redis(host=HOST, port=PORT, password=PASS)
    pub = r.pubsub()
    pub.subscribe(CHANNEL)

    while True:
        urls_obj = find_urls_should_add_queue_2()
        if urls_obj is not None:
            for url_obj in urls_obj:
                logging.info("Select from Queue_1: " + url_obj['url'])
                # append to queue layer 2

                push_queue_layer_2(url_obj)

        # data = pub.get_message()
        # if data:
        #     # print(data)
        #     message = data['data']
        #     if message and message != 1:
        #         logging.info("Message: " + message.decode('utf-8'))

        time.sleep(5)
