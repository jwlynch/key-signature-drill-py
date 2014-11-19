import unittest
from key import Key

class TestKey(unittest.TestCase):
    
    def testKeyTextAnswer(self):
        key_txt_list = []
        key_txt_list.append(['C#', '7 sharps'])
        key_txt_list.append(['F#', '6 sharps'])
        key_txt_list.append(['B', '5 sharps'])
        key_txt_list.append(['E', '4 sharps'])
        key_txt_list.append(['A', '3 sharps'])
        key_txt_list.append(['D', '2 sharps'])
        
        key_txt_list.append(['Cb', '7 flats'])
        key_txt_list.append(['Gb', '6 flats'])
        key_txt_list.append(['Db', '5 flats'])
        key_txt_list.append(['Ab', '4 flats'])
        key_txt_list.append(['Eb', '3 flats'])
        key_txt_list.append(['Bb', '2 flats'])
        
        key_txt_list.append(['F', '1 flat'])
        key_txt_list.append(['C', 'no sharps or flats'])
        key_txt_list.append(['G', '1 sharp'])
        
        for key_txt in key_txt_list:
            self.assertEqual(Key(key_txt[0])._text_answer(), key_txt[1])

    def testAccidentals(self):
        sharps = ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']
        flats = ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
        sharp_keys = ['C#', 'F#', 'B', 'E', 'A', 'D', 'G']
        flat_keys = ['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
        
        key_acc_list = []
        
        for i in range(1, 7):
            key_acc_list.append([sharp_keys[i], sharps[:-i]])
            key_acc_list.append([flat_keys[i], flats[:-i]])
        
        key_acc_list.append(['C#', sharps])
        key_acc_list.append(['Cb', flats])
        
        key_acc_list.append(['C', []])
        
        for key_acc in key_acc_list:
            self.assertEqual(Key(key_acc[0]).accidentals(), key_acc[1])

if __name__ == '__main__':
    unittest.main()
