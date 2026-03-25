import unittest
from lab3_2sem import BinaryTree, is_tree_balanced


class TestBinaryTreeBalance(unittest.TestCase):
    def test_1_b(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        result = is_tree_balanced(root)
        print(f"Тест 1 - {'Збалансовано' if result else 'Незбалансовано'}")
        self.assertTrue(result)

    def test_2_unb(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)

        result = is_tree_balanced(root)
        print(f"Тест 2 - {'Збалансовано' if result else 'Незбалансовано'}")
        self.assertFalse(result)

    def test_3_empt(self):
        result = is_tree_balanced(None)
        print(f"Тест 3 - {'Збалансовано' if result else 'Незбалансовано'}")
        self.assertTrue(result)

    def test_4_single(self):
        root = BinaryTree(10)
        result = is_tree_balanced(root)
        print(f"Тест 4 - {'Збалансовано' if result else 'Незбалансовано'}")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()