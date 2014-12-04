#!/usr/bin/env python

from keysigquestion import KeySigQuestion

lop = True

while lop:
    q = KeySigQuestion()
    
    try:
        goodBool = q.ask()
    except KeyboardInterrupt:
        # maybe print stats here
        break
    finally:
        if goodBool:
            print "Right!"
        else:
            print "Wrong!"
