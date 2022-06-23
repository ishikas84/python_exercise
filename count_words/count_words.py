import string


def count_words(sentence):
    count_dict = {}
    sp_chars = "".join([x for x in string.punctuation if x != "'"]) + "¿"
    sentence = sentence.translate(str.maketrans("", "", sp_chars))
    for word in sentence.split():
        word = word.lower()
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
