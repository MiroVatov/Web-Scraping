import sqlite3

conn = sqlite3.connect('myquotes.db')  # Creates the database, if it is not created already
curr = conn.cursor()  # Creates the connection with the DB

# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 teg text)""")

#  RUN the above script just once, in order the database to be created. If you run it more times, it will throw an error(DB already exist).

curr.execute("""insert into quotes_tb values ('Python is awsome', 'build_with_python', 'python')""")

conn.commit()  # COMMIT
conn.close()  # Closing the connection after execution of the SQL commands
