import mysql.connector

try:
  book_store_db = mysql.connector.connect(
  host= 'localhost',
  user= 'root',
  passwd = '#############',
)
except mysql.connector.Error:
  print("Database could not connect, Please check your logins")
else:
  book_store_db_cursor = book_store_db.cursor()
  book_store_db_cursor.execute(
    "CREATE DATABASE IF NOT EXISTS alx_book_store"
  )
  book_store_db.commit()

  book_store_db_cursor.execute("USE alx_book_store")
  book_store_db.commit()

  print(f"Database {book_store_db.database} created successfully!")
finally:
  book_store_db.close()
