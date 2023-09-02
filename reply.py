import pywhatkit as kit
import time

# Replace with the recipient's phone number (including the country code)
recipient_number = "+233202334725"

# Replace with the message you want to send as an automated reply
reply_message = "Thank you for your message. I will get back to you soon."

# Check for incoming messages and send automated replies
while True:
    try:
        kit.check_for_new_messages()
        time.sleep(100)  # Check for new messages every 10 seconds

        # Send an automated reply to the latest message
        kit.sendwhatmsg(recipient_number, reply_message, 0, 0)
    except Exception as e:
        print("An error occurred:", str(e))
