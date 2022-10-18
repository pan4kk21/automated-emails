import yagmail
import pandas
import datetime
from news import NewsFeed
import time


send_hour = YOUR_HOUR
send_minute = YOUR_MINUTE


def send_email():
    global news
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    news = NewsFeed(row["interest"],
                    yesterday,
                    today)
    email = yagmail.SMTP(user="pan4kkpan4@gmail.com", password="inigkcawslvuuxmx")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']}, \n See what's on about {row['interest']} today. \n\n {news.get()}\nPavel Melnik")


while True:
    if datetime.datetime.now().hour == send_hour and datetime.datetime.now().minute == send_minute:

        df = pandas.read_excel("people.xlsx")

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)