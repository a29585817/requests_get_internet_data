import smtplib
import datetime as dt
import random
my_email = "Your mail"
password = "Your password"



now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)


with open("quotes.txt", mode="r") as file:
    data = [x.strip() for x in file.readlines()]

quote = random.choice(data)

while True:
    if day_of_week == 2:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="a07044011195@gmail.com",
                                msg=f"Subject:Go ahead\n\n{quote}")
            break

