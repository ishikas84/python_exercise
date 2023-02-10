from itertools import islice
import time
def window(s:str, n: int):
    s = iter(s)
    result = tuple(islice(s, n))
    if len(result) == n:
        yield "".join(result)
    for elem in s:
        result = result[1:] + (elem,)
        yield "".join(result)



def langestPalindrome(s:str) -> str:

    window_size = len(s)
    while window_size > 0:
        result = window(s, window_size)
        for elem in result:
            if elem[0] != elem[-1]:
                continue
            total = len(elem)
            half = int(total / 2)
            if total % 2 == 0:
                if elem[:half] == elem[half:][::-1]:
                    return elem
            else:
                if elem[:half+1] == elem[half:][::-1]:
                    return elem

        window_size -= 1
    return s

s = "kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd"

a = time.perf_counter()
print(langestPalindrome(s))
print(time.perf_counter() - a)
