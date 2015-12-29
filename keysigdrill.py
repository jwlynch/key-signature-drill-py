#!/usr/bin/env python

from keysigquestion import KeySigQuestion

try:
    while True:
        q = KeySigQuestion()
        if q.ask():
            print ("Right!")
        else:
            print ("Wrong! the correct answer was {0}".format{q.correctAns})
except KeyboardInterrupt:
    # maybe print stats here
    print()

