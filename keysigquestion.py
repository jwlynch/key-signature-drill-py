import random
from key import Key

class KeySigQuestion(object):
    def __init__(self):
        self.itsKey = Key()

    def ask(self):
        choice = []
        choice.append(self.givenKeyGiveAccidentals)
        choice.append(self.givenSignatureGiveKey)
        choice.append(self.givenAccidentalsGiveKey)
        return random.choice(choice)()

    def givenKeyGiveAccidentals(self):
        q = "What's the key signature of " + self.itsKey.key[0] + "? "
        a = raw_input(q).strip()
        result = (a == self.itsKey._text_answer())
        
        return result
    
    def givenSignatureGiveKey(self):
        q = "What key has " + self.itsKey._text_answer() + "? "
        a = raw_input(q).strip()
        result = (a == self.itsKey.key[0])
        
        return result

    def givenAccidentalsGiveKey(self):
        q = "What key has " + self.itsKey.accidentals() + "? "
        a = raw_input(q).strip()
        result = (a == self.itsKey.key[0])
        
        return result