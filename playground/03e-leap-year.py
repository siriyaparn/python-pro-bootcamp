# Write a program that works out whether if a given year is a leap year.
# This is how you work out whether if a particular year is a leap year.
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder

# Which year do you want to check?
year = int(input())

# Method 1
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# Method 2
if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")