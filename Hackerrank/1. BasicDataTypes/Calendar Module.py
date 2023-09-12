import calendar
m, d, y = map(int, input().split())
# print(calendar.day_name[calendar.weekday(y, m, d)].upper())
n = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
day_number = calendar.weekday(y, m ,d)
print(n[day_number])
