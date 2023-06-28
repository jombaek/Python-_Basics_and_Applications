import datetime

year, month, day = map(int, input().split())
days = int(input())

start = datetime.date(year, month, day)
end = start + datetime.timedelta(days)

print(end.year, end.month, end.day)