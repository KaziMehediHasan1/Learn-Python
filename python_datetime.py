import datetime

"""current_time = datetime.datetime.now()
print("Current date and time:", current_time)
print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)
print("Weekday (0=Monday, 6=Sunday):", current_time.weekday())
# Adding 5 days to the current date
# 
# # Format date to a different string format
# YYYY/MM/DD
current_time = datetime.datetime.now()
# YYY/dd/MM
formatted_date1 = current_time.strftime("%Y/%d/%m")
print("Formatted date (YYYY/MM/DD):", formatted_date1)
#  dd/mm/YYYY
formatted_date2 = current_time.strftime("%d/%m/%Y  %H:%M:%S")
print("Formatted date (dd/mm/YYYY):", formatted_date2)"""

#  calculating the difference between two dates
dateOne = datetime.datetime(2022, 5, 17)
dateTwo = datetime.datetime(2023, 6, 18)

difference = dateTwo - dateOne
print("Difference between", dateTwo.date(), "and", dateOne.date(), "is", difference, "days")

new_date = dateOne + datetime.timedelta(days=45)
print("New date after adding 45 days to", dateOne.date(), "is", new_date.date())

