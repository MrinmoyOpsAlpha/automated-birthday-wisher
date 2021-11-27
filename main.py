import smtplib

my_email="mrinmoysingha7002@gmail.com"
password="opsai@123"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail (
            from_addr=my_email,     
            to_addrs="mrinmoysingha7002@yahoo.com",    
            msg="Subject:Hello\n\n This is the original body message!"
         )
