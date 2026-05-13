import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from lab9_2sem import build_prefix_function, kmp_search


class TestBuildPrefixFunction(unittest.TestCase):

    def test_no_repeating_pattern(self):
        self.assertEqual(build_prefix_function("abcd"), [0, 0, 0, 0])

    def test_classic_kmp_pattern(self):
        self.assertEqual(build_prefix_function("ababaca"), [0, 0, 1, 2, 3, 0, 1])


class TestKmpSearch(unittest.TestCase):

    def test_single_occurrence(self):
        self.assertEqual(kmp_search("hello world", "world"), [6])

    def test_multiple_occurrences(self):
        self.assertEqual(kmp_search("ababab", "ab"), [0, 2, 4])

    def test_overlapping_occurrences(self):
        self.assertEqual(kmp_search("aaaa", "aa"), [0, 1, 2])

    def test_no_occurrence(self):
        self.assertEqual(kmp_search("hello", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(kmp_search("hello", ""), [])

    def test_unicode(self):
        self.assertEqual(kmp_search("привіт привіт", "привіт"), [0, 7])

    def test_type_error(self):
        with self.assertRaises(TypeError):
            kmp_search(123, "abc")


if __name__ == "__main__":
    unittest.main()