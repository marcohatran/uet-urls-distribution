import psycopg2


class PostgresState:
    connection = None

    @staticmethod
    def get_connection():
        if PostgresState.connection:
            return PostgresState.connection
        else:
            PostgresState.connection = psycopg2.connect(user="postgres",
                                                        password="UETDistribute!@#2019",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        # database="uet_distribute_url")
                                                        database="postgres")
            return PostgresState.connection
