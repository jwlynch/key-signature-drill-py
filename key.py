import random

class Key(object):
    sharps = ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']
    flats = ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
    thekeys = \
      {
        "C#": [[7, "sharps"], ["C#", "D#", "E#", "F#", "G#", "A#", "B#"]],
        "F#": [[6, "sharps"], ["F#", "G#", "A#", "B", "C#", "D#", "E#"]],
        "B": [[5, "sharps"], ["B", "C#", "D#", "E", "F#", "G#", "A#"]],
        "E": [[4, "sharps"], ["E", "F#", "G#", "A", "B", "C#", "D#"]],
        "A": [[3, "sharps"], ["A", "B", "C#", "D", "E", "F#", "G#"]],
        "D": [[2, "sharps"], ["D", "E", "F#", "G", "A", "B", "C#"]],
        "G": [[1, "sharps"], ["G", "A", "B", "C", "D", "E", "F#"]],
        "C": [[0, "no sharps or flats"], ["C", "D", "E", "F", "G", "A", "B"]],
        "F": [[1, "flats"], ["F", "G", "A", "Bb", "C", "D", "E"]],
        "Bb": [[2, "flats"], ["Bb", "C", "D", "Eb", "F", "G", "A"]],
        "Eb": [[3, "flats"], ["Eb", "F", "G", "Ab", "Bb", "C", "D"]],
        "Ab": [[4, "flats"], ["Ab", "Bb", "C", "Db", "Eb", "F", "G"]],
        "Db": [[5, "flats"], ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"]],
        "Gb": [[6, "flats"], ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"]],
        "Cb": [[7, "flats"], ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"]],
      }

    def _assemble_key(self, key):
      if key in self.thekeys.keys():
        result = []
        result.append(key)
        for i in self.thekeys[key]:
          result.append(i)
      else:
        print "key " + key + " could not be found"
      
      return result
    
    def _text_answer(self):
      theKey = self.key[1]
      if theKey[0] == 0:
        result = theKey[1]
      elif theKey[0] == 1:
        result = "1 " + theKey[1][:-1]
      else:
        result = str(theKey[0]) + " " + theKey[1]
      
      return result
    
    def accidentals(self):
        return [] # oass
     
    def __init__(self, aKey=None):
      if aKey is None:
        self.key = self._assemble_key(random.choice(self.thekeys.keys()))
      elif aKey in self.thekeys.keys():
        self.key = self._assemble_key(aKey)

    def mode(self, mode_num):
      scale = self.key[1]
      themode = scale[mode_num:] + scale[:mode_num]
      return themode

