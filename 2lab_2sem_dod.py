import unittest

def get_min_board_size(n, w, h):
    min_len = max(w, h)
    max_len = max(w, h) * n
    ww_len = max_len
    iterations = 0

    while min_len <= max_len:
        iterations += 1
        mid_len = (min_len + max_len) // 2
        
        if mid_len == 0:
            min_len = mid_len + 1
            continue
            
        found_ww_len = (mid_len // w) * (mid_len // h)
        
        if found_ww_len >= n:
            ww_len = mid_len
            max_len = mid_len - 1
        else:
            min_len = mid_len + 1
            
    print(f"Мінімальний розмір дошки: {ww_len}")
    print(f"Кількість ітерацій: {iterations}")  
    return ww_len

class TestBoardSize(unittest.TestCase):
    
    def test_example_1(self):
        self.assertEqual(get_min_board_size(10, 2, 3), 9)

    def test_example_2(self):
        self.assertEqual(get_min_board_size(2, 1000000000, 999999999), 1999999998)

    def test_example_3(self):
        self.assertEqual(get_min_board_size(4, 1, 1), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)