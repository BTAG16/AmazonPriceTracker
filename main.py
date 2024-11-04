import os
import smtplib
import time
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

amazon_headers = {
    get the User-Agent by pasting [https://httpbin.org/headers] in your browser
}

amazon_URL = "{Get a Product of your choice from the Amazon website.}"

def price_tracker():
    response = requests.get(amazon_URL, headers=amazon_headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find(name="span", id="productTitle").getText()
    currency = soup.find(name="span", class_="a-offscreen").getText()[:1]
    price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
    target_price = 45.00

    sender = os.environ["SENDER"]
    password = os.environ["PASSWORD"]
    receiver = os.environ["RECEIVER"]

    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "Amazon Price Alert!!!"
    message.set_content(f"{title} is now {currency}{price}\n\n\n\n\n\n\n\n{amazon_URL}")

    if price < target_price:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user=sender, password=password)
        server.send_message(message)
        server.close()
        print("Alert Sent.")
    else:
        print("Nothing!")

while True:
    price_tracker()
    time.sleep(1800)
