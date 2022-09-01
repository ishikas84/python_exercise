def _convert_int(date1):
    date1_list = date1.split("/")
    date1_list = [date1_list[-1], *date1_list[:-1]]
    return int("".join(date1_list))


def get_earliest(*dates):
    int_detes_list = [_convert_int(date) for date in dates]
    min_index = int_detes_list.index(min(int_detes_list))
    return dates[min_index]


print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))
