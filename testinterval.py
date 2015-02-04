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

if __name__ == '__main__':
    unittest.main()
