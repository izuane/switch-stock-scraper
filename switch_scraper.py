# Tutorial used: https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development (Option 2: Using .starttls())


import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import time
from email.mime.text import MIMEText

from dotenv import load_dotenv

import os

load_dotenv()
SMTP_SERVER = os.getenv("SMTP_SERVER")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")
RECEIVER_EMAIL_1 = os.getenv("RECEIVER_EMAIL_1")
RECEIVER_EMAIL_2 = os.getenv("RECEIVER_EMAIL_2")

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def check_smyths_AC_switch_stock():
    global URL_smyths_AC_switch
    URL_smyths_AC_switch = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/nintendo-gaming/nintendo-switch/nintendo-switch-consoles/nintendo-switch-animal-crossing-limited-edition-console/p/187118'
    soup = get_soup(URL_smyths_AC_switch)

    mydivs = soup.findAll("p", class_="deliveryType homeDelivery js-stockStatus")

    stock_message = str(mydivs[0])
    stock_message = stock_message.lower()

    # If we can't find "out of stock" then assume it is in stock
    return stock_message.find("out of stock") == -1


def check_smyths_neon_switch_stock():
    global URL_smyths_neon_switch
    URL_smyths_neon_switch = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/nintendo-gaming/nintendo-switch/nintendo-switch-consoles/nintendo-switch-neon-red-blue-with-improved-battery-life/p/182022'
    soup = get_soup(URL_smyths_neon_switch)

    mydivs = soup.findAll("p", class_="deliveryType homeDelivery js-stockStatus")

    stock_message = str(mydivs[0])
    stock_message = stock_message.lower()

    # If we can't find "out of stock" then assume it is in stock
    return stock_message.find("out of stock") == -1


def check_smyths_grey_switch_stock():
    global URL_smyths_grey_switch
    URL_smyths_grey_switch = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/nintendo-gaming/nintendo-switch/nintendo-switch-consoles/nintendo-switch-grey-with-improved-battery-life/p/182023'
    soup = get_soup(URL_smyths_grey_switch)

    mydivs = soup.findAll("p", class_="deliveryType homeDelivery js-stockStatus")

    stock_message = str(mydivs[0])
    stock_message = stock_message.lower()

    # If we can't find "out of stock" then assume it is in stock
    return stock_message.find("out of stock") == -1


def check_nintendo_AC_switch_stock():
    global URL_nintendo_AC_switch
    URL_nintendo_AC_switch = 'https://store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-animal-crossing-new-horizons-edition/12458084.html'
    soup = get_soup(URL_nintendo_AC_switch)

    mybutton = soup.find("button", {"data-component": "productAddToBasket"})

    stock_message = mybutton.text
    stock_message = stock_message.lower()

    # If we can't find "out of stock" then assume it is in stock
    return stock_message.find("out of stock") == -1


def check_nintendo_neon_switch_stock():
    global URL_nintendo_neon_switch
    URL_nintendo_neon_switch = 'https://store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-with-neon-blue-neon-red-joy-con-controllers/12245286.html'
    soup = get_soup(URL_nintendo_neon_switch)

    mybutton = soup.find("button", {"data-component": "productAddToBasket"})

    stock_message = mybutton.text
    stock_message = stock_message.lower()

    # If we can't find "out of stock" then assume it is in stock
    return stock_message.find("out of stock") == -1


def check_nintendo_grey_switch_stock():
    global URL_nintendo_grey_switch
    URL_nintendo_neon_switch = 'https://store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-with-neon-blue-neon-red-joy-con-controllers/12245286.html'
    soup = get_soup(URL_nintendo_neon_switch)

    mybutton = soup.find("button", {"data-component": "productAddToBasket"})

    stock_message = mybutton.text
    stock_message = stock_message.lower()

    # If we can't find "out of stock" then assume it is in stock
    return stock_message.find("out of stock") == -1


def check_JL_AC_switch_stock():
    global URL_JL_AC_switch
    URL_JL_AC_switch = 'https://www.johnlewis.com/nintendo-switch-1-1-console-with-animal-crossing-new-horizons-game-bundle/p4918594'
    soup = get_soup(URL_JL_AC_switch)

    mybutton = soup.find("button", {"id": "button--add-to-basket"})

    # JL has separate buttons for in stock and out of stock
    # If we can't find "in stock" (i.e. "add to basket") button, meaning soup returns None, then in_stock will be False
    return (mybutton is not None)


def check_JL_neon_switch_stock():
    global URL_JL_neon_switch
    URL_JL_neon_switch = 'https://www.johnlewis.com/nintendo-switch-1-1-32gb-console-with-joy-con/neon/p4751133'
    soup = get_soup(URL_JL_neon_switch)

    mybutton = soup.find("button", {"id": "button--add-to-basket"})

    # JL has separate buttons for in stock and out of stock
    # If we can't find "in stock" (i.e. "add to basket") button, meaning soup returns None, then in_stock will be False
    return (mybutton is not None)


def check_JL_grey_switch_stock():
    global URL_JL_grey_switch
    URL_JL_grey_switch = 'https://www.johnlewis.com/nintendo-switch-1-1-32gb-console-with-joy-con/grey/p4751133'
    soup = get_soup(URL_JL_grey_switch)

    mybutton = soup.find("button", {"id": "button--add-to-basket"})

    # JL has separate buttons for in stock and out of stock
    # If we can't find "in stock" (i.e. "add to basket") button, meaning soup returns None, then in_stock will be False
    return (mybutton is not None)


while True:

    smyths_AC_switch_stock = check_smyths_AC_switch_stock()
    smyths_neon_switch_stock = check_smyths_neon_switch_stock()
    smyths_grey_switch_stock = check_smyths_grey_switch_stock()

    nintendo_AC_switch_stock = check_nintendo_AC_switch_stock()
    nintendo_neon_switch_stock = check_nintendo_neon_switch_stock()

    JL_AC_switch_stock = check_JL_AC_switch_stock()
    JL_neon_switch_stock = check_JL_neon_switch_stock()
    JL_grey_switch_stock = check_JL_grey_switch_stock()

    # For testing

    # smyths_AC_switch_stock = True
    # smyths_neon_switch_stock = True
    # smyths_grey_switch_stock = True
    #
    # nintendo_AC_switch_stock = True
    # nintendo_neon_switch_stock = True
    #
    # JL_AC_switch_stock = True
    # JL_neon_switch_stock = True
    # JL_grey_switch_stock = True

    # This will be true if any one of them is true
    # Later on, we will only send links if one of the variables is true
    in_stock = smyths_AC_switch_stock or smyths_neon_switch_stock or smyths_grey_switch_stock \
               or nintendo_AC_switch_stock or nintendo_neon_switch_stock \
               or JL_AC_switch_stock or JL_neon_switch_stock or JL_grey_switch_stock

    if in_stock:
        smtp_server = SMTP_SERVER
        port = 587  # For starttls
        sender_email = SENDER_EMAIL
        receiver_emails = [RECEIVER_EMAIL_1, RECEIVER_EMAIL_2]

        # Multiple recepients msg
        email_msg = ""

        # Smyths
        if smyths_AC_switch_stock:
            email_msg += """

                         Smyths Animal Crossing
            """ \
                         + URL_smyths_AC_switch \
                         + """

              """

        if smyths_neon_switch_stock:
            email_msg += """

                         Smyths neon
            """ \
                         + URL_smyths_neon_switch \
                         + """

              """

        if smyths_grey_switch_stock:
            email_msg += """

                         Smyths grey
            """ \
                         + URL_smyths_grey_switch \
                         + """

              """

        # Nintendo
        if nintendo_AC_switch_stock:
            email_msg += """

                        Nintendo Animal Crossing
            """ \
                         + URL_nintendo_AC_switch \
                         + """

             """

        if nintendo_neon_switch_stock:
            email_msg += """

                        Nintendo neon
            """ \
                         + URL_nintendo_neon_switch \
                         + """

             """

        # John Lewis
        if JL_AC_switch_stock:
            email_msg += """

                        JL Animal Crossing:
            """ \
                         + URL_JL_AC_switch \
                         + """

            """
        if JL_neon_switch_stock:
            email_msg += """

                        JL neon:
            """ \
                         + URL_JL_neon_switch \
                         + """

            """

        if JL_grey_switch_stock:
            email_msg += """

                        JL grey:
            """ \
                         + URL_JL_grey_switch \
                         + """

            """

        msg = MIMEText(email_msg)

        msg['Subject'] = "SWITCH IN STOCK"
        msg['From'] = sender_email
        msg['To'] = ", ".join(receiver_emails)

        password = SENDER_EMAIL_PASSWORD

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)

            server.sendmail(sender_email, receiver_emails, msg.as_string())

            print("EMAIL SENT")
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    time.sleep(30)
