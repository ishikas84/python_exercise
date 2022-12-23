import datetime
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=3):
    dt = datetime.date(year, month, 1)
    prev = dt - datetime.timedelta(days=1)
    flag = False
    if nth < 0:
        nth = nth % 4 - nth
        flag = True
    # if isinstance(weekday, Enum):
    #     weekday = weekday.value
    adj = (weekday - dt.weekday()) % 7
    dt += datetime.timedelta(days=adj)
    dt += datetime.timedelta(weeks=nth - 1)
    print(prev.day, dt.day)
    if flag and ( 8>= (prev.day - dt.day) >= 7 or dt.month == 3):
        dt += datetime.timedelta(weeks=1)
    return dt


print(meetup_date(2012, 3))
print(meetup_date(2015, 2))
print(meetup_date(2018, 6))
print(meetup_date(2020, 1))
print(meetup_date(2015, 8))
print("SD Python:", meetup_date(2015, 8, nth=4, weekday=3))
print("PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=2))
print("SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=1))

print("SDHN on last Friday:", meetup_date(2010, 6, nth=-1, weekday=4))
print("-1 != 4 (sometimes):", meetup_date(2020, 1, nth=-1, weekday=4))

print("SDJS", meetup_date(2012, 2, nth=1, weekday=Weekday.TUESDAY))
print("PyLadies", meetup_date(2018, 7, nth=2, weekday=Weekday.WEDNESDAY))
print("SDHN", meetup_date(2010, 6, nth=-1, weekday=Weekday.FRIDAY))

print(meetup_date(2018, 3, nth=-1, weekday=5))
print(meetup_date(2018, 1, nth=-2, weekday=0))
print(meetup_date(2018, 6, nth=-1, weekday=Weekday.SATURDAY))