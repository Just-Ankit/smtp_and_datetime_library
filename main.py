import smtplib
import datetime as dt
import random

my_email = "ankit@gmail.com"
password = "akdjlkajf"
receiver_email = "ankitpython01@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Birthday Wisher/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=f"Subject: Monday Quotes\n\n{quote}"
        )


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=receiver_email,
#                         msg="Subject:Hello\n\nThis is the body of my email")


