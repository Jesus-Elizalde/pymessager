from imessage_reader import fetch_data
from dotenv import dotenv_values

config = dotenv_values(".env")

DB_PATH = config["MESSAGEDB"]

# Create a FetchData instance
fd = fetch_data.FetchData(DB_PATH)

# Store messages in my_data
# This is a list of tuples containing user id, message and service (iMessage or SMS).
messages = fd.get_messages()
print(messages[1][1])
