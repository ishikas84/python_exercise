
class FuzzyString:
    def __init__(self, sentence):
        self.sentence = sentence

    def __eq__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() == other.sentence.lower()
        else:
            return self.sentence.lower() == other.lower()

    def __repr__(self):
        return repr(self.sentence)

    def __str__(self):
        return self.sentence

    def __lt__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() < other.sentence.lower()
        else:
            return self.sentence.lower() < other.lower()

    def __gt__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() > other.sentence.lower()
        else:
            return self.sentence.lower() > other.lower()

    def __le__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() <= other.sentence.lower()
        else:
            return self.sentence.lower() <= other.lower()

    def __ge__(self, other):
        if isinstance(other, FuzzyString):
            return self.sentence.lower() >= other.sentence.lower()
        else:
            return self.sentence.lower() >= other.lower()

    def __contains__(self, other):
        if isinstance(other, FuzzyString):
            return other.sentence.lower() in self.sentence.lower()
        else:
            return other.lower() in self.sentence.lower()

    def __add__(self, other):
        if isinstance(other, FuzzyString):
            return FuzzyString(self.sentence + other.sentence)
        else:
            return FuzzyString(self.sentence + other)