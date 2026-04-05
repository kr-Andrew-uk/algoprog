import unittest
from lab4_2sem import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def test_single_tree(self):
        pq = RedBlackPriorityQueue()
        
        items_to_insert = [
            ("Task A", 5), ("Task B", 6), ("Task C", 4), 
            ("Task D", 8), ("Task E", 9), ("Task F", 7), 
            ("Task G", 2), ("Task K", 1), ("Task K", 3)
        ]
        
        for val, prio in items_to_insert:
            pq.insert(val, prio)
        print(f"Маєм {len(items_to_insert)} елементів.")

        top = pq.peek()
        print(f"Найвищий пріоритет: {top}")
        self.assertEqual(top, ("Task E", 9))

        expected_priorities = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        
        for expected_prio in expected_priorities:
            extracted = pq.extract_max()
            print(f"    Дістали: {extracted}")
            self.assertEqual(extracted[1], expected_prio)

        self.assertIsNone(pq.extract_max())
        print("Черга порожня, тест пройдено")

if __name__ == '__main__':
    unittest.main()