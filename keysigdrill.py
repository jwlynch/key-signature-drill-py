#!/usr/bin/env python

from keysigquestion import KeySigQuestion

try:
    while True:
        q = KeySigQuestion()
        if q.ask():
            print "Right!"
        else:
            print "Wrong!"
except KeyboardInterrupt:
    # maybe print stats here
    print

