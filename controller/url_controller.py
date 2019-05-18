import logging

from helper.postgres_helper import execute_without_response, execute
from state.postgres_state import PostgresState

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


def find_url(url):
    query = f"""
    SELECT * FROM url WHERE url LIKE '{url}'
    """
    connecttion = PostgresState.get_connection()
    results = execute(connecttion, query)
    if len(results) > 0:
        return results[0]
    else:
        return None


def create_new_url(url_obj):
    if find_url(url_obj['url']) is None:
        query_insert = f"""
         INSERT INTO url (host, url, status, piority, rank) VALUES (
         '{url_obj['host']}', '{url_obj['url']}', '{url_obj['status']}', '{url_obj['piority']}', '{url_obj['rank']}'
         );
        """
        connection = PostgresState.get_connection()
        execute_without_response(connection, query_insert)
    else:
        logging.info('crawled ' + url_obj['url'])


def find_urls_should_add_queue_2():
    query = """
    SELECT * FROM url WHERE status_id <= 1 
    ORDER BY 
    piority desc,
    updated_at asc    
    """
    connection = PostgresState.get_connection()
    results = execute(connection, query)
    return results


def update_status(url_obj):
    query = f"""
    UPDATE url SET 
        status = '{url_obj['status']}',
        status_id = '{url_obj['status_id']}'
    WHERE url = '{url_obj['url']}'
    """
    connection = PostgresState.get_connection()
    execute_without_response(connection, query)
