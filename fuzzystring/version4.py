import unicodedata


class FuzzyString:
    def __init__(self, sentence):
        self.sentence = sentence
        
    def unicode_norm(self, sentence):
        return unicodedata.normalize("NFD", sentence.casefold())
    
    def __eq__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() == other.sentence.lower()
        else:
            return self.unicode_norm(self.sentence.lower()) == self.unicode_norm(other.lower())

    def __repr__(self):
        return repr(self.sentence)

    def __str__(self):
        return self.sentence

    def __lt__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() < other.sentence.lower()
        else:
            return self.unicode_norm(self.sentence.lower()) < self.unicode_norm(other.lower())

    def __gt__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() > other.sentence.lower()
        else:
            return self.unicode_norm(self.sentence.lower()) > self.unicode_norm(other.lower())

    def __le__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() <= other.sentence.lower()
        else:
            return self.unicode_norm(self.sentence.lower()) <= self.unicode_norm(other.lower())

    def __ge__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() >= other.sentence.lower()
        else:
            return self.unicode_norm(self.sentence.lower()) >= self.unicode_norm(other.lower())

    def __contains__(self, other):
        if isinstance(other, FuzzyString):
            return other.sentence.lower() in self.sentence.lower()
        else:
            return self.unicode_norm(other.lower()) in self.unicode_norm(self.sentence.lower())

    def __add__(self, other):
        if isinstance(other, FuzzyString):
            return FuzzyString(self.sentence.lower() + other.sentence.lower())
        else:
            return FuzzyString(self.unicode_norm(self.sentence.lower()) + self.unicode_norm(other.lower()))
        