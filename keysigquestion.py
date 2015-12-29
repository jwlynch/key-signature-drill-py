import random
from key import Key

PY2 = (str is bytes)

if PY2:
    my_input = raw_input
else:
    my_input = input

class KeySigQuestion(object):
    def __init__(self, aKey=None):
        if aKey is None:
            self.itsKey = Key()
        else:
            self.itsKey = Key(aKey)

        self.majorKeyName = self.itsKey.key[0]

    def ask(self):
        choice = []
        choice.append(self.givenKeyGiveAccidentals)
        choice.append(self.givenSignatureGiveKey)
        choice.append(self.givenAccidentalsGiveKey)
        return random.choice(choice)()

    def givenKeyGiveAccidentals(self):
        self.q = "What's the key signature of " + self.majorKeyName + "? "
        self.correctAns = self.itsKey.textual_key_signature()
        self.a = my_input(self.q).strip()
        result = (self.a == self.correctAns)
        
        return result
    
    def givenSignatureGiveKey(self):
        self.q = "What key has " + self.itsKey.textual_key_signature() + "? "
        self.correctAns = self.majorKeyName
        self.a = my_input(self.q).strip()
        result = (self.a == self.correctAns)
        
        return result

    def givenAccidentalsGiveKey(self):
        self.q = "What key has " + ", ".join(self.itsKey.accidentals()) + "? "
        self.correctAns = self.majorKeyName
        self.a = my_input(self.q).strip()
        result = (self.a == self.correctAns)
        
        return result
