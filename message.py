import pywhatkit as kit

number = "+233202334725"  # Replace with the recipient's phone number (including the country code)

# Send a WhatsApp message at midnight
kit.sendwhatmsg(
    number,
    'Happy Birthday!',
    0, 0  # Midnight
)
