from os import replace
import smtplib,datetime as dt,pandas,random

my_email="mrinmoysingha7002@gmail.com"
password="opsai@123"

today_tuple=(dt.datetime.now().month,dt.datetime.now().day)

data=pandas.read_csv("day 32/birthdays.csv")

birthday_dict={ ( data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()  }

if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"day 32/letter templates/letter{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.google.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:HAPPY BIRTHDAY\n\n{contents}"
            )




