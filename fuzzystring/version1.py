class FuzzyString:
    def __init__(self, sentence):
        self.sentence = sentence

    def __eq__(self, other):
        if len(self.sentence) == len(other):
            return self.sentence.lower() == other.lower()
        return False

    def __repr__(self):
        return repr(self.sentence)

    def __str__(self):
        return self.sentence
