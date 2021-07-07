import sqlite3

conn = sqlite3.connect('amazon_scraping.db')  # Creates the database, if it is not created already
curr = conn.cursor()  # Creates the connection with the DB
#
# curr.execute("""create table amazon_tb(
#                 product_name text,
#                 product_author text,
#                 product_imagelink link)""")

#  RUN the above script just once, in order the database to be created. If you run it more times, it will throw an error(DB already exist).

curr.execute("""insert into amazon_tb values('Python is awsome', 'build_with_python', 'python')""")

conn.commit()  # COMMIT

conn.close()  # Closing the connection after execution of the SQL commands