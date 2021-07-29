##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "Your mail"
password = "Your password"

now = dt.datetime.now()
now_day = now.day
now_month = now.month
print(now_day)
print(now_month)

#=---------------------get birthdays list --------------------
df = pd.read_csv("birthdays.csv")
df_dict = df.to_dict(orient="records")
print(df_dict)

#-----------------------------Get letter--------------------------
file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
# -------------------compair-----------------
for x in df_dict:
    if now_day == x["day"] and now_month == x["month"]:
        with open(file_path ,mode="r") as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", x["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=x["email"],
                                msg=f"Subject:Happy birthday\n\n{contents}")
