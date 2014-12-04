#!/usr/bin/env python

from keysigquestion import KeySigQuestion

lop = True

while lop:
    goodBool = False
    q = KeySigQuestion()
    
    try:
        goodBool = q.ask()
    except KeyboardInterrupt:
        # maybe print stats here
        lop = False
    finally:
        if lop:
            if goodBool:
                print "Right!"
            else:
                print "Wrong!"
