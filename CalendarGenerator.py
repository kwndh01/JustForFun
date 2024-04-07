//CalendarGenerator
//Version: 1.0
//Date: 2024-04-07

def leap(year):
  if (year % 4 == 0):
    if (year % 100 == 0):
      if (year % 400 == 0 or year % 400 == 100):
        leap_var = 1
      else:
        leap_var = 0
    else:
      leap_var = 1
  else:
    leap_var = 0
  return leap_var


def setCalendar(j):
  month = [30] * 12
  for i in range(0, 12, 2):
    month[i] = 31
  if (j == 1):
    month[1] = 29
  else:
    month[1] = 28
  return month


# make default so that we can calculate distance
default_year = 2024
default_month = 1

# user input
year = int(input("year: "))
month = int(input("month: "))

# check leap yeaer
is_leap_year = leap(year)

# total days in input month
days_in_month = setCalendar(is_leap_year)[month - 1]

# calculate distance from default year and month
navigation = 0
if year < default_year:
  for i in range(year, default_year):
    if leap(i):
      navigation -= 366
    else:
      navigation -= 365
  for i in range(1, month):
    navigation += setCalendar(leap(year))[i - 1]
elif year == default_year:
  for i in range(1, month):
    navigation += setCalendar(leap(year))[i - 1]

# calculate the day of the week the selected month starts
starting_point = (navigation + 1) % 7

# print
print(f"{month}/{year}")
print(" S  M  T  W  T  F  S")
print("   " * starting_point, end="")
for i in range(1, days_in_month + 1):
  print(f"{i:2d}", end=" ")
  if (i + starting_point) % 7 == 0:
    print()
