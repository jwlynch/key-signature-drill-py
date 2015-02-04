import unittest
from interval import Interval

class TestInterval(unittest.TestCase):
    
    def testSomeIntervals(self):
        mi_2 = Interval(2, "mi", False)
        ma_2 = Interval(2, "Ma", False)
        mi_3 = Interval(3, "mi", False)
        ma_3 = Interval(3, "Ma", False)
        mi_6 = Interval(6, "mi", False)
        ma_6 = Interval(6, "Ma", False)
        mi_7 = Interval(7, "mi", False)
        ma_7 = Interval(7, "Ma", False)

        p_1 = Interval(1, "p", True)
        p_4 = Interval(4, "p", True)
        a_4 = Interval(4, "a", True)
        p_5 = Interval(5, "p", True)
        d_5 = Interval(5, "d", True)

        self.assertEqual(str(mi_2), "minor second or ninth")
        self.assertEqual(str(ma_2), "major second or ninth")
        self.assertEqual(str(mi_3), "minor third or tenth")
        self.assertEqual(str(ma_3), "major third or tenth")
        self.assertEqual(str(mi_6), "minor sixth or thirteenth")
        self.assertEqual(str(ma_6), "major sixth or thirteenth")
        self.assertEqual(str(mi_7), "minor seventh")
        self.assertEqual(str(ma_7), "major seventh")

        self.assertEqual(str(p_1), "perfect unison or octave")
        self.assertEqual(str(p_4), "perfect fourth or eleventh")
        self.assertEqual(str(a_4), "augmented fourth or eleventh")
        self.assertEqual(str(p_5), "perfect fifth or twelvth")
        self.assertEqual(str(d_5), "diminished fifth or twelvth")

    def testBasicIntervalTable(self):
        mi_2 = Interval(2, "mi", False)
        ma_2 = Interval(2, "Ma", False)
        mi_3 = Interval(3, "mi", False)
        ma_3 = Interval(3, "Ma", False)
        mi_6 = Interval(6, "mi", False)
        ma_6 = Interval(6, "Ma", False)
        mi_7 = Interval(7, "mi", False)
        ma_7 = Interval(7, "Ma", False)

        p_1 = Interval(1, "p", True)
        p_4 = Interval(4, "p", True)
        a_4 = Interval(4, "a", True)
        p_5 = Interval(5, "p", True)
        d_5 = Interval(5, "d", True)

        letter_list = ["C", "D", "E", "F", "G", "A", "B"]

        table_list = [Interval(x, y) for x in letter_list for y in letter_list]

        interval_list = \
        [
            p_1, ma_2, ma_3, p_4, p_5, ma_6, ma_7,
            mi_7, p_1, ma_2, mi_3, p_4, p_5, ma_6,
            mi_6, mi_7, p_1, mi_2, mi_3, p_4, p_5,
            p_5, ma_6, ma_7, p_1, ma_2, ma_3, a_4,
            p_4, p_5, ma_6, mi_7, p_1, ma_2, ma_3,
            mi_3, p_4, p_5, mi_6, mi_7, p_1, ma_2,
            mi_2, mi_3, p_4, d_5, mi_6, mi_7, p_1
        ]

        for dex in range(len(interval_list)):
            #print
            #(
            #    str(dex) +
            #    " " +
            #    str(interval_list[dex]) +
            #    " " +
            #    str(table_list[dex])
            #)
            self.assertEqual(interval_list[dex], table_list[dex])

if __name__ == '__main__':
    unittest.main()
