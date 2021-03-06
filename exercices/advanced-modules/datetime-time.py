import datetime

time = datetime.time(22, 4, 17)

print("Time Created: " + str(time))
print("Hours: " + str(time.hour))
print("Minutes: " + str(time.minute))
print("Seconds: " + str(time.second))
print("Microseconds: " + str(time.microsecond))
print("Time Zone Info: " + str(time.tzinfo))

print("\nEarliest Time: " + str(datetime.time.min))
print("Latest Time: "  + str(datetime.time.max))
print("Time Resolution: "  + str(datetime.time.resolution))
