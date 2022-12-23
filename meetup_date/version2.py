import datetime


def meetup_date(year, month, nth=4, weekday=3):
    dt = datetime.date(year, month, 1)
    adj = (weekday - dt.weekday()) % 7
    dt += datetime.timedelta(days=adj)
    dt += datetime.timedelta(weeks=nth - 1)
    return dt


print(meetup_date(2012, 3))
print(meetup_date(2015, 2))
print(meetup_date(2018, 6))
print(meetup_date(2020, 1))
print(meetup_date(2015, 8))
print("SD Python:", meetup_date(2015, 8, nth=4, weekday=3))
print("PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=2))
print("SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=1))