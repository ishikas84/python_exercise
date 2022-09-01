def get_earliest(date1, date2):
    date1_list = date1.split("/")
    date1_list = [date1_list[-1], *date1_list[:-1]]
    date1_int = int("".join(date1_list))
    date2_list = date2.split("/")
    date2_list = [date2_list[-1], *date2_list[:-1]]
    date2_int = int("".join(date2_list))
    return date2 if date1_int >= date2_int else date1


print(get_earliest("01/27/1832", "01/27/1756"))
print(get_earliest("02/29/1972", "12/21/1946"))
print(get_earliest("02/24/1946", "03/21/1946"))
print(get_earliest("06/21/1958", "06/24/1958"))
