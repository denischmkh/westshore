import time

from selenium.webdriver.common.by import By

from load_django import *
from parser_app.models import CharterRecordWestshore
from selenium.webdriver import Chrome

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'          # или smtp.yandex.ru, smtp.mail.ru и т.п.
SMTP_PORT = 587
EMAIL_FROM = 'osvspotfixtures@gmail.com'
EMAIL_PASSWORD = 'psws gkmr xskb zvgp'
EMAIL_TO = 'osvspotfixtures@gmail.com'

url = 'https://westshore.no/'

browser = Chrome()

browser.get(url=url)
time.sleep(3)

table_block = browser.find_element(by=By.XPATH, value='//tbody[@data-reactid=".0.1.0.0.1.1.1.1:$0.0.0.2.0.0.0.1"]')

rows = table_block.find_elements(by=By.XPATH, value='./tr')

def send_notification_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)
        print("📧 Email has been send successfully.")
    except Exception as e:
        print(f"❌ Error while sending email: {e}")

for row in rows:
    tds = [el.text for el in row.find_elements(by=By.XPATH, value='./td')]
    date, vessel, charterer, scope_of_work, comm, rate = tds
    print(f'Date: {date}')
    print(f'Vessel: {vessel}')
    print(f'Charterer: {charterer}')
    print(f'Scope of Work: {scope_of_work}')
    print(f'Comm.: {comm}')
    print(f'Rate: {rate}')
    print(f'')
    record, created = CharterRecordWestshore.objects.get_or_create(
        date=date,
        vessel=vessel,
        charterer=charterer,
        scope_of_work=scope_of_work,
        comm=comm,
        rate=rate
    )
    if created:
        subject = f"Westshore: {vessel}"
        body = (
            f"Date: {date}\n"
            f"Vessel: {vessel}\n"
            f"Charterer: {charterer}\n"
            f"Scope of Work: {scope_of_work}\n"
            f"Comm.: {comm}\n"
            f"Rate: {rate}\n"
        )
        print(f"✅ New Record: {vessel}")
        send_notification_email(subject, body)
    else:
        print(f"ℹ️ Already exists: {vessel}")


