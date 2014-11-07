#!/usr/bin/env python

from keysigquestion import KeySigQuestion

lop = True

while lop:
    q = KeySigQuestion()
    goodBool = q.ask()
    
    if goodBool:
      print "Right!"
    else:
      print "Wrong!"
