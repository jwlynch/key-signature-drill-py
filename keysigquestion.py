from key import Key

class KeySigQuestion(object):
    def __init__(self):
        self.itsKey = Key()

    def ask(self):
        return self.givenKeyGiveAccidentals()

    def givenKeyGiveAccidentals(self):
        q = "What's the key signature of " + self.itsKey.rand_key[0] + "? "
        a = raw_input(q)
        result = (a == self.itsKey.rand_key[1])
        
        return result