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
            self.assertEqual(Key(key_txt[0])._text_answer() == key_txt[1]

if __name__ == '__main__':
    unittest.main()
