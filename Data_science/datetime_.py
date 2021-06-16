'''There are three classes in date time module
Date and Time class
datetime class
timedelta class
'''
#date and time class
#date class has three mandatory attribute year, month and day
'''
MINYEAR<=year<=Maxyear
1<=month<=12
1<=day<=number of days in the given month
'''
#import datetime
from datetime import date, time, datetime, timedelta

mydate = date(year = 1998, month = 7, day = 19 )
print("date is: ",mydate,'\n')

print(date.today())
print(time(12,14,22))

#datetime class
mydate = datetime(year = 1998, month = 7, day = 19 )
print("date is: ",mydate,'\n')

print(datetime.now())

#timedelta class is used to calculating diffrernces in dates and is used for date manipulation
todays_date = datetime.now()
dateafter_months = todays_date + timedelta(days=90)
print(dateafter_months)
