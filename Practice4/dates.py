from datetime import datetime

# Get current date and time

x = datetime.now()
print(x)

# Create specific date

y = datetime(2024, 1, 1)
print(y)

# Format date

print(x.strftime("%A"))       # Weekday
print(x.strftime("%B"))       # Month name
print(x.strftime("%Y"))       # Year

# Calculate difference

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 1, 10)

difference = date2 - date1
print(difference.days)