import pymysql.cursors

def createConnectionDB() -> any:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Lopez2905.",
        database="infoclientesdb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection
