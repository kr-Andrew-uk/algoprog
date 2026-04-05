import unittest
from lab1_2sem import find_unsorted_subarray

class TestUnsortedSubarray(unittest.TestCase):
    def test_spaceship(self):
        array = list(range(100, 50, -1))
        array[20:30] = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
        start, end = find_unsorted_subarray(array, descending=True)
        print(f"{len(array)} {start} {end}")
        
        self.assertTrue(len(array) >= 50)
        self.assertNotEqual((start, end), (-1, -1))

if __name__ == '__main__':
    unittest.main()