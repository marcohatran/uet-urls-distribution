import logging

from helper.postgres_helper import execute_without_response, execute
from state.postgres_state import PostgresState

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


def find_hosts():
    query = """
    SELECT * FROM host 
    ORDER BY 
    rank desc ,
    updated_at asc    
    """
    connection = PostgresState.get_connection()
    results = execute(connection, query)
    return results
