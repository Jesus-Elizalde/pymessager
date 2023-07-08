from imessage_reader import fetch_data
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

DB_PATH = config["MESSAGEDB"]

RECIPIENT_NUMBER = config["RECIPIENT_NUMBER"] # I suggest adding yours initially to test
MESSAGE = "'Whats up doc'"

# Create a FetchData instance
fd = fetch_data.FetchData(DB_PATH)

# Store messages in my_data
# This is a list of tuples containing user id, message and service (iMessage or SMS).
messages = fd.get_messages()
print(messages[1][1])
os.system("osascript sendMessage.applescript {} {}".format(RECIPIENT_NUMBER, MESSAGE))
