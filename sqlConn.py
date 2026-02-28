import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    dbname="mydatabase"
)

cursor = conn.cursor()

# Create the tasks table if it doesn't exist
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS tasks (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         status VARCHAR(50)
#     )
# """)
#
# # Insert sample records
# cursor.execute("INSERT INTO tasks (name, status) VALUES (%s, %s)", ("Task 1", "Pending"))
# cursor.execute("INSERT INTO tasks (name, status) VALUES (%s, %s)", ("Task 2", "Completed"))
# cursor.execute("INSERT INTO tasks (name, status) VALUES (%s, %s)", ("Task 3", "In Progress"))
# 
# conn.commit()  # Save changes

# Query and print all records
cursor.execute("SELECT * FROM tasks")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()