import datetime


def meetup_date(year, month):
    dt = datetime.date(year, month, 1)
    first_w = dt.isoweekday()
    if first_w == 7:
        first_w = 0
    elif first_w == 6:
        first_w = -1
    elif first_w == 5:
        first_w = -2
    th_4 = 26 - first_w
    return datetime.date(year, month, th_4)


print(meetup_date(2012, 3))
print(meetup_date(2015, 2))
print(meetup_date(2018, 6))
print(meetup_date(2020, 1))
print(meetup_date(2015, 8))