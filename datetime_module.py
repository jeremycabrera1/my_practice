from datetime import datetime
now = datetime.now()
new_years = datetime(year= now.year + 1, month=1, day=1)
difference = new_years - now
days_left = difference.days
print(days_left)