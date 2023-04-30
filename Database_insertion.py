"""
This is experimental code for how the connection between
this project and potential database can look like.

Check out the "Optional_table.sql" file in the main directory
for the table.
"""

import psycopg2
from start import contact, username, user

# Connect to the database
conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")

# Open a cursor to perform database operations
cur = conn.cursor()

# Define the insert statement
insert_statement = "INSERT INTO Users (login, name, creation_date) VALUES (%s, %s, %s)"

# Extract values from the contact_info dictionary
name = contact.get("name")
creation_date = user.created_at_str

# Execute the insert statement with the extracted values
cur.execute(insert_statement, (username, name, creation_date))

# Commit the changes to the database
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()

