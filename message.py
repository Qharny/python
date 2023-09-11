# import pywhatkit as kit

# number = "+233202334725"  # Replace with the recipient's phone number (including the country code)

# # Send a WhatsApp message at midnight
# kit.sendwhatmsg(
#     number,
#     'Hello!',
#     0, 0  # Midnight
# )

import pywhatkit as kit
import time

number = "+233202334725"  # Replace with the recipient's phone number (including the country code)
message = "Hello!"

# Calculate the current time in seconds since the epoch
current_time = time.time()

# Calculate the time for sending the message in 1 minute (60 seconds later)
send_time = current_time + 20

# Use a while loop to wait until it's time to send the message
while time.time() < send_time:
    pass

# Send the message after the 1-minute delay
kit.sendwhatmsg(
    number,
    message,
    0, 0  # Midnight
)
