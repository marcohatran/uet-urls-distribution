import logging

from state.postgres_state import PostgresState
from helper.postgres_helper import execute, execute_without_response

HOST = 'localhost'
PORT = '6379'
PASS = 'UETDistribute!@#2019'
CHANNEL = 'QUEUE_LAYER_1'

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


def create_new_host(host_obj):
    query_insert = f"""
     INSERT INTO host (host, piority, rank) VALUES ('{host_obj['host']}', '{host_obj['piority']}', '{host_obj[
        'rank']}');
    """
    logging.info(query_insert)
    connection = PostgresState.get_connection()
    execute_without_response(connection, query_insert)


def find_host(host):
    connection = PostgresState.get_connection()
    query = f"SELECT * FROM host WHERE host LIKE '{host}'"
    rows = execute(connection, query)
    if rows and len(rows) == 1:
        return rows[0]
    else:
        return None


def calculate_host_piority(host):
    return 3


def get_host_status(host):
    host_obj = find_host(host)
    if host_obj:
        return host_obj
    else:
        host_obj = {'host': host, 'piority': 5, 'rank': calculate_host_piority(host)}
        create_new_host(host_obj)
        return find_host(host)

# get_host_status('vnexpress.net')
# host_obj = {'host': 'zing.vn', 'piority': 5}
# create_new_host(host_obj)
