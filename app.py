from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open WhatsApp Web
baseurl = "https://web.whatsapp.com"
driver.get(baseurl)

# Wait for QR Code scan (increase sleep time if needed)
print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(10)

# Read contacts and messages from the CSV file
with open('contacts.csv', newline='') as csvfile:
    readContacts = csv.reader(csvfile)
    next(readContacts)  # Skip the header row
    
    for phone, msg in readContacts:
        phonnum = phone
        message = msg

        # Construct the WhatsApp URL for the contact
        sameTab = (baseurl + '/send?phone=' + str(phonnum))
        driver.get(sameTab)

        # Wait for the chat to load (increase sleep time if necessary)
        time.sleep(8)

        # Find the message input field and send the message
        content = driver.switch_to.active_element
        content.send_keys(message)
        content.send_keys(Keys.RETURN)

        # Add a delay to avoid potential errors due to quick navigation
        time.sleep(8)

# Close the browser
driver.quit()