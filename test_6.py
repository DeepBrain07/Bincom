import psycopg2
from psycopg2 import sql
import urllib.parse as urlparse

# get the colours worn on Monday and put them in a list
monday_colours = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
monday_colours = monday_colours.split(", ")

# get the colours worn on Tuesday and put them in a list
tuesday_colours = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE"
tuesday_colours = tuesday_colours.split(", ")

# get the colours worn on Wednesday and put them in a list
wednesday_colours = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE"
wednesday_colours = wednesday_colours.split(", ")

# get the colours worn on Thursday and put them in a list
thursday_colours = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
thursday_colours = thursday_colours.split(", ")

# get the colours worn on Friday and put them in a list
friday_colours = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
friday_colours = friday_colours.split(", ")

# create a dict with day of the week as the key and list of colours worn on that day as value
days = {"monday": monday_colours, "tuesday": tuesday_colours, "wednesday": wednesday_colours, "thursday": thursday_colours, "friday": friday_colours}

colours = {}

# get the number of times a colour was repeated in a day
for d in list(days.keys()):
    for colour in days[d]:
        if colour in list(colours.keys()):
            colours[colour] += 1
        else:
            colours[colour] = 1

database_url = "postgres://yilvvlax:v3EuTzEVgjrNrKFYB-yHhMcNNAm6utHW@raja.db.elephantsql.com/yilvvlax"

# Parse the URL to get individual connection parameters
url = urlparse.urlparse(database_url)

# Use psycopg2 to connect with the parsed parameters
connection = psycopg2.connect(
    database=url.path[1:],  # remove the leading '/' from the path
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


cursor = connection.cursor()

# Data to be inserted into the table (example)
data = [(k, v) for k, v in colours.items()]


create_table_query = """
CREATE TABLE IF NOT EXISTS my_table (
    colour VARCHAR(50) PRIMARY KEY,
    frequency INT
);
"""
cursor.execute(create_table_query)

# Commit the transaction
connection.commit()

insert_query = """
    INSERT INTO my_table (colour, frequency)
    VALUES (%s, %s)
    ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
"""

cursor.executemany(insert_query, data)

# Commit the transaction
connection.commit()

# Print a success message
print("Data inserted successfully!")

# Close the cursor and connection
cursor.close()
connection.close()
