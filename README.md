# switch-stock-scraper
A simple python script to send an email alert when a Nintendo Switch is online from select UK retailers.

You will need a .env file in the same directory as this script with the following variables:

```
SMTP_SERVER="smtp.email.co.uk"
SENDER_EMAIL="sender@email.co.uk"
SENDER_EMAIL_PASSWORD="password"
RECEIVER_EMAILS='["receiver1@email.co.uk", "receiver2@email.co.uk"]'
```
