"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# initial variables for month and year
today = datetime.now()
month = today.month
year = today.year

# initial variable for cal(text calendar)
cal = calendar.TextCalendar(firstweekday=6)

#grabbing sys arguments
sys_args = sys.argv
length = len(sys_args)

# function to print cal for given month
def print_cal(y, m):
  print(cal.formatmonth(y, m))

# check month and date input are valid
def check_date(m = month, y = year):
  if(0 < int(m) <= 12 and 1 <= int(y) <= 9999):
    print_cal(int(y), int(m))
  elif(0 > int(m) or int(m) > 12):
    print('Invalid input!\nMonth must a number between 1 - 12')
  else:
    print('Invalid input!\nYear must be a number between 1 - 9999')


# Print calendar based on input
if (length == 1):
  print_cal(year, month)
elif (length == 2):
  check_date(sys_args[1])
else:
  check_date(sys_args[1], sys_args[2])
