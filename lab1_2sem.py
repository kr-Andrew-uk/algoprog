import unittest

def find_unsorted_subarray(array, descending=False):
    n = len(array)
    if n <= 1:
        return (-1, -1)

    def is_correct_order(a, b):
        if descending:
            return a >= b
        return a <= b

    Llim = 0
    while Llim < n - 1 and is_correct_order(array[Llim], array[Llim + 1]):
        Llim += 1

    if Llim == n - 1:
        return (-1, -1)
    
    Rlim = n - 1
    while Rlim > 0 and is_correct_order(array[Rlim - 1], array[Rlim]):
        Rlim -= 1
        
    sub = array[Llim : Rlim + 1]
    mas_min = min(sub)
    mas_max = max(sub)

    if descending:
        while Llim > 0 and array[Llim - 1] < mas_max:
            Llim -= 1
        while Rlim < n - 1 and array[Rlim + 1] > mas_min:
            Rlim += 1
    else:
        while Llim > 0 and array[Llim - 1] > mas_min:
            Llim -= 1
        while Rlim < n - 1 and array[Rlim + 1] < mas_max:
            Rlim += 1

    return (Llim, Rlim)

class TestUnsortedSubarray(unittest.TestCase):

    def test_already_sorted(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4, 5]), (-1, -1))

    def test_full_sort_needed(self):
        self.assertEqual(find_unsorted_subarray([5, 4, 3, 2, 1]), (0, 4))

    def test_single_element(self):
        self.assertEqual(find_unsorted_subarray([10]), (-1, -1))

if __name__ == '__main__':
    unittest.main()