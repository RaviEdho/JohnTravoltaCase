import unittest
import JohnTravolta
from JohnTravolta import OutOfRangeLowerBoundError
from JohnTravolta import OutOfRangeUpperBoundError

class Testcode(unittest.TestCase):

    def testCase1(self):
        self.assertEqual(JohnTravolta.tabungan(52, 600000), "Dapat menabung sebesar Rp270000.")

    def testCase2(self):
        self.assertEqual(JohnTravolta.tabungan(30, 200000), "Dapat menabung sebesar Rp250000.")

    def testCase3(self):
        self.assertEqual(JohnTravolta.tabungan(40, 600000), "Anda tidak dapat menabung.")

    def testCase4(self):
        self.assertEqual(JohnTravolta.tabungan(50, 1000000), "Cari tambahan pekerjaan lain.")

    def testCase5(self):
        with self.assertRaises(OutOfRangeLowerBoundError):
            JohnTravolta.totalGaji(-1)

    def testCase6(self):
        with self.assertRaises(OutOfRangeUpperBoundError):
            JohnTravolta.totalGaji(169)

    def testCase7(self):
        with self.assertRaises(TypeError):
            JohnTravolta.totalGaji(52.1)

    def testCase8(self):
        with self.assertRaises(TypeError):
            JohnTravolta.totalGaji("abc")

    def testCase9(self):
        with self.assertRaises(OutOfRangeLowerBoundError):
            JohnTravolta.tabungan(40, -100000)

    def testCase10(self):
        with self.assertRaises(TypeError):
            JohnTravolta.tabungan(40, 100000.1)

    def testCase11(self):
        with self.assertRaises(TypeError):
            JohnTravolta.tabungan(40, "abc")

if __name__ == '__main__':
    unittest.main()