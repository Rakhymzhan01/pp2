from datetime import datetime, timedelta
#Write a Python program to subtract five days from current date.

current_date = datetime.now()

five_days_ago = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Five Days Ago:", five_days_ago.strftime("%Y-%m-%d"))

#Write a Python program to print yesterday, today, tomorrow.
current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#Write a Python program to drop microseconds from datetime.

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)

#Write a Python program to calculate two date difference in seconds.

date1 = datetime(2024, 2, 23, 22, 32, 0)  # date 1
date2 = datetime(2024, 2, 22, 12, 0, 0)  # date 2

time_difference_seconds = abs((date1 - date2).total_seconds())

print("Difference in seconds:", time_difference_seconds)