import json
import logging
import random
import time

from urllib.parse import urlparse

from datetime import datetime
import redis

from controller.url_controller import create_new_url
from helper.sitemap_helper import get_url_from_sitemap
from worker.get_rank_host import get_host_status

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


def get_urls():
    urls = get_url_from_sitemap('https://vnexpress.net/articles-2019-sitemap.xml?m=4&d=24')
    return urls


def calculate_url_piority(url):
    return random.uniform(2, 4.5)


if __name__ == '__main__':

    urls = get_urls()
    for url in urls:
        logging.info('prepare add ' + url)
        host = urlparse(url).netloc
        now = datetime.now()
        timestamp = int(datetime.timestamp(now))
        host_obj = get_host_status(host)

        create_new_url(
            {'url': url, 'host': host_obj['host'], 'piority': host_obj['piority'], 'status': 'added_queue_1',
             'status_id': 1, 'rank': calculate_url_piority(url)})

        time.sleep(5)
