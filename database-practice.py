import psycopg2

connection = psycopg2.connect(database="learning", user="postgres", password="gregg1.", host="localhost", port="5434")
cursor = connection.cursor()
cursor.execute("SELECT * FROM purchases")
for row in cursor:
    print(row)