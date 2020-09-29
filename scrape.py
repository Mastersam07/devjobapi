import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "mastersam",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "devjobhub")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    # cursor = connection.cursor()
    
    # Select all from table jobs_job
    create_table_query = '''SELECT * FROM jobs_job; '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table fetched successfully in PostgreSQL\n")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print('Done checking!!!')

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")