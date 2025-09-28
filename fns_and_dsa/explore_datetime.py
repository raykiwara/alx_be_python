#script that performs specified operations with dates and times

import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    now = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {now}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(number_of_days):
    current_date = datetime.datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

calculate_future_date(number_of_days)
