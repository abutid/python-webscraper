# python application that trackers the product on amazon and notifies you via email
# if price has gone down

import re
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.parser import BytesParser, Parser
from email.policy import default

URL = 'https://www.amazon.com/dp/B07K97BQDF/ref=us_comp_a_ip_xr_5c008'

#give information about the browser
header = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}



def analyze_price():
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    convert_price = price[0:4]
    convert_price = re.sub('[$]', '', convert_price)
    convert_price = int(convert_price)
    print(title)
    print(convert_price)

    if(convert_price < 700):
       send_mail()

    print(convert_price)
    print(title.strip())

    if(convert_price > 700):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()       # for connecting and identifying the connection for email
    server.starttls()   # encrypts connection
    server.ehlo()

    server.login('rasbian33@gmail.com', 'Trolls1212')

    subject = 'Price dropped!'
    body = 'Check the link to see the the reduced price https://www.amazon.com/dp/B07K97BQDF/ref=us_comp_a_ip_xr_5c008'
    print('hello')

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'rasbian33@gmail.com',
        'danny_antonelli@outlook.com',
        message
    )

    print('Amazon Price Tracker Email Has Been Sent')
#
# def email(to_email, subject, message, servor='smtp.gmail.con'):


    server.quit()


analyze_price()





