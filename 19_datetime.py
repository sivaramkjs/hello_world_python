from datetime import datetime, timezone, timedelta

current_datetime = datetime.now(timezone.utc)
print(current_datetime)

date_time = datetime(2026, 9, 23, 13, 0, 0)
print(date_time)

date_time_from_str = datetime.strptime('2023-09-23 14:00', '%Y-%m-%d %H:%M')
print(date_time_from_str)

# start = timedelta(hours=1, minutes=30)
# end = timedelta(hours=0, minutes=30)
start = datetime.strptime('1:30', '%H:%M')
end = datetime.strptime('0:30', '%H:%M')
if end < start:  # cross midnight across days handling
    end += timedelta(days=1)
print(end - start)
