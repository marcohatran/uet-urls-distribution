def execute_without_response(connection, query):
    cursor = connection.cursor()
    try:
        create_table_query = query
        cursor.execute(create_table_query)
        connection.commit()

    except Exception as e:
        print(e)
        connection.rollback()

    # finally:
    #     # closing database connection.
    #     if connection:
    #         if cursor:
    #             cursor.close()
    #         cursor.close()
    #         connection.close()
    #         # print("PostgreSQL connection is closed")


def execute(connection, query):
    cursor = connection.cursor()
    try:
        create_table_query = query
        cursor.execute(create_table_query)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
    except Exception as e:
        print(e)
        connection.rollback()
    # finally:
    #     # closing database connection.
    #     if connection:
    #         if cursor:
    #             cursor.close()
    #         connection.close()
    #         # print("PostgreSQL connection is closed")
    return None
