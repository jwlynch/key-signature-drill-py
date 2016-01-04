import random
from majScales import majScales
from interval import Interval

PY2 = (str is bytes)

majScalesList = majScales()

if PY2:
    my_input = raw_input
else:
    my_input = input

class IntervalQuestion(object):
    def __init__(self):
        scale = random.choice(majScalesList)
        self.highNote  = random.choice(scale)
        self.lowNote = random.choice(scale)
        self.interval = Interval(self.lowNote, self.highNote)

    def ask(self):
        choice = []
        choice.append(self.givenLowNoteAndIntervalGiveHighNote)
        return random.choice(choice)()

    def givenLowNoteAndIntervalGiveHighNote(self):
        q = "What note is a {0} above {1}? ".format(self.interval, self.lowNote)
        a = my_input(q).strip()
        result = (a == self.highNote)
        self.correctAns = self.highNote
        
        return result
    
