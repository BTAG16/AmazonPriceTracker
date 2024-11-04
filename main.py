import os
import smtplib
import time
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

amazon_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

amazon_URL = "https://www.amazon.com/Leather-Platform-Loafers-Classic-Business/dp/B0CP898J2X/ref=sr_1_1?crid=3GSIG5K1B5OTF&dib=eyJ2IjoiMSJ9.8TcvggvgyCN4vQNTy4ctyigDH7xRoBn33THsTH63iyKNQKZ8k7ok_pZIFgzQLZXjZPHx2P2fG-7NysxLAJ-rAYzniakseezPMYy-NU2S_886r1-HT6sFj9v1bQfd3Y3ej7E-PBtVY_-iq3EwFkQ6CLMfQj4mT1x1A0mTM01ieiKpMrYsJWRKk_sRh_dP2RLhwrkzlX_9HnJZf9MIa9W-ScLJxGznDQ8wXSBWRj5T_qgRauTBe_Jt6Q0RGrmhoXq6ZMD5erUu0wY_t3TDQqgAb3AyLXopGe7EmN8i6JAV86Y.AptsaP6J0Fpv-fD77BhMdYnJa-NpRzrA0QUCCvCtdtk&dib_tag=se&keywords=chunky%2Bloafers%2Bfor%2Bmen&psr=EY17&qid=1730710791&s=todays-deals&sprefix=chunky%2Bloafers%2Ctodays-deals%2C169&sr=1-1-catcorr&th=1"

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