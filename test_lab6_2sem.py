import unittest
from lab6_2sem import solve


class TestBeerSolver(unittest.TestCase):

    def test_example_1(self):
        data = "2 2\nYN NY"
        self.assertEqual(solve(data), 2)

    def test_example_2(self):
        data = "6 3\nYNN YNY YNY NYY NYY NYN"
        self.assertEqual(solve(data), 2)

    def test_one_beer_covers_all(self):
        data = "3 3\nYNN YNN YNN"
        self.assertEqual(solve(data), 1)

    def test_every_employee_unique_beer(self):
        data = "3 3\nYNN NYN NNY"
        self.assertEqual(solve(data), 3)

    def test_one_employee_one_beer(self):
        data = "1 1\nY"
        self.assertEqual(solve(data), 1)

    def test_one_employee_multiple_beers(self):
        data = "1 3\nY Y Y"
        self.assertEqual(solve(data), 1)

    def test_all_like_all(self):
        data = "4 4\nYYYY YYYY YYYY YYYY"
        self.assertEqual(solve(data), 1)

    def test_two_groups_no_overlap(self):
        data = "4 2\nYN YN NY NY"
        self.assertEqual(solve(data), 2)

    def test_three_beers_need_two(self):
        data = "3 3\nYNN NNY NNY"
        self.assertEqual(solve(data), 2)


if __name__ == '__main__':
    unittest.main()