##Extra Hard Version
import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import pandas

load_dotenv()

my_email = os.getenv("my_email")
password = os.getenv("password")

data = pandas.read_csv("birthdays.csv")
data.columns = data.columns.str.strip()

now =dt.datetime.now()
current_month = now.month
current_day = now.day
#
# print(current_month)
# print(current_day)

for index, row in data.iterrows():
    birth_month = row['birth_month']
    birth_day = row['birth_day']

    if current_month == birth_month and current_day == birth_day:

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row['email'],
                msg = "Subject:Hello\n\nHappy Birthday"
            )