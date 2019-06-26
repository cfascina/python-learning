import datetime

today = datetime.date.today()

print("Current Date: " + str(today))
print("\nComplete Date: " + str(today.ctime()))
print("Date Tuple: " + str(today.timetuple()))
print("Date as Ordinal: " + str(today.toordinal()))
print("Year: " + str(today.year))
print("Month: " + str(today.month))
print("Day: " + str(today.day))

print("\nEarliest Date: " + str(datetime.date.min))
print("Latest Date: "  + str(datetime.date.max))
print("Date Resolution: "  + str(datetime.date.resolution))

print("\nCurrent Date: " + str(today))
print("Year Changed to 2001 w/ replace(): "  + str(today.replace(year = 2001)))

date_1 = datetime.date(1989, 5, 17)
date_2 = datetime.date(1990, 11, 14)
print("\nDate 1: " + str(date_1))
print("Date 2: " + str(date_2))
print("Dates Difference: " + str(date_2 - date_1))
