import datetime


def meetup_date(year, month, nth=4, weekday=3):
    dt = datetime.date(year, month, 1)
    prev = dt - datetime.timedelta(days=1)
    flag = False
    if nth < 0:
        nth = nth % 4 - nth
        flag = True
    adj = (weekday - dt.weekday()) % 7
    dt += datetime.timedelta(days=adj)
    dt += datetime.timedelta(weeks=nth - 1)
    if flag and ((prev.day - dt.day) == 7 or dt.month == 3):
        dt += datetime.timedelta(weeks=1)
    return dt