import smtplib
import datetime as dt
import random

with open("day 32/quotes.txt") as quotes_file:
    all_quotes=quotes_file.readlines()
    quote=random.choice(all_quotes)
    

my_email="mrinmoysingha7002@gmail.com"
password="opsai@123"


now=dt.datetime.now()
weekday=now.weekday()

if weekday==5:
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail (
                from_addr=my_email,     
                to_addrs="mrinmoysingha7002@yahoo.com",    
                msg=f"Subject:WEEKLY  SCHEDULED MOTIVATIONAL QUOTE \n\n {quote}!"
            )
