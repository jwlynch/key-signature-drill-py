import random
from interval import Interval

PY2 = (str is bytes)

if PY2:
    my_input = raw_input
else:
    my_input = input

class IntervalQuestion(object):
    def __init__(self, aKey=None, aChro=None, aLoNote=None):
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
        q = "What's the key signature of " + self.majorKeyName + "? "
        a = my_input(q).strip()
        result = (a == self.itsKey.textual_key_signature())
        
        return result
    
    def givenSignatureGiveKey(self):
        q = "What key has " + self.itsKey.textual_key_signature() + "? "
        a = my_input(q).strip()
        result = (a == self.majorKeyName)
        
        return result

    def givenAccidentalsGiveKey(self):
        q = "What key has " + ", ".join(self.itsKey.accidentals()) + "? "
        a = my_input(q).strip()
        result = (a == self.majorKeyName)
        
        return result