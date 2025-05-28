import time

from selenium.webdriver.common.by import By

from load_django import *
from parser_app.models import CharterRecordBraemaroffshore
from selenium.webdriver import Chrome

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'          # или smtp.yandex.ru, smtp.mail.ru и т.п.
SMTP_PORT = 587
EMAIL_FROM = 'osvspotfixtures@gmail.com'
EMAIL_PASSWORD = 'psws gkmr xskb zvgp'
EMAIL_TO = 'osvspotfixtures@gmail.com'

url = 'https://www.braemaroffshore.com/'



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
while True:
    browser = Chrome()

    browser.maximize_window()

    browser.get(url=url)
    time.sleep(5)

    table_block = browser.find_element(by=By.ID, value='fixturesTableDesktop')
    browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", table_block)
    time.sleep(10)

    rows = table_block.find_elements(by=By.XPATH, value='.//tr[@class="datarow"]')
    for row in rows:
        tds = [el.text for el in row.find_elements(by=By.XPATH, value='./td')]
        date, vessel, charterer, scope_of_work, asset, period, onhire, rate, *other = tds
        print(f'Date: {date}')
        print(f'Vessel: {vessel}')
        print(f'Charterer: {charterer}')
        print(f'Scope of Work: {scope_of_work}')
        print(f'Asset: {asset}')
        print(f'Period: {period}')
        print(f'Onhire: {onhire}')
        print(f'Rate: {rate}')
        print(f'')
        record, created = CharterRecordBraemaroffshore.objects.get_or_create(
            date=date,
            vessel=vessel,
            charterer=charterer,
            scope_of_work=scope_of_work,
            asset=asset,
            period=period,
            onhire=onhire,
            rate=rate
        )
        if created:
            subject = f"Braemar: {vessel}"
            body = (
                f"Date: {date}\n"
                f"Vessel: {vessel}\n"
                f"Charterer: {charterer}\n"
                f"Scope of Work: {scope_of_work}\n"
                f"Asset: {asset}\n"
                f"Period: {period}\n"
                f"Onhire: {onhire}\n"
                f"Rate: {rate}\n"
            )
            print(f"✅ New Record: {vessel}")
            send_notification_email(subject, body)
        else:
            print(f"ℹ️ Already exists: {vessel}")
    browser.close()
    time.sleep(10800)
