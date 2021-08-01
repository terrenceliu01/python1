from sqlitehelper import create_connection, create_table
"""
Create books table in sqlitebook.db database
"""
def main():
    database = "sqlitebook.db"
    
    sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (
                                        _id text PRIMARY KEY,
                                        title text NOT NULL,
                                        author text,
                                        read boolean,
                                        price real,
                                        rating integer
                                    ); """

    conn = create_connection(database)
    if conn is not None:
        try:
            # create projects table
            create_table(conn, sql_create_books_table)
        except Exception as error:
            print(f"Error: {error}" )

if __name__ == '__main__':
    main()
    print("Done.")