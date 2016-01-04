#!/usr/bin/env python

from intervalquestion import IntervalQuestion

try:
    while True:
        q = IntervalQuestion()
        if q.ask():
            print ("Right!")
        else:
            print ("Wrong! the correct answer was {0}".format(q.correctAns))
except KeyboardInterrupt:
    # maybe print stats here
    print()

