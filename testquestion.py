import unittest
from keysigquestion import KeySigQuestion
from key import Key

class TestQuestion(unittest.TestCase):
    def testMajorKeyName(self):
        testKeys = ['C#', 'F#', 'B', 'E', 'A', 'D', 'G', 'C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
        
        for aKey in testKeys:
            self.assertEqual(aKey, KeySigQuestion(aKey).majorKeyName)

if __name__ == '__main__':
    unittest.main()
