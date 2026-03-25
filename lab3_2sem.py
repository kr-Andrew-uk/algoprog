class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _get_height(node: BinaryTree) -> int:
    if node is None:
        return 0

    left_height = _get_height(node.left)
    if left_height == -1:
        return -1 

    right_height = _get_height(node.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1
def is_tree_balanced(node: BinaryTree) -> bool:
    return _get_height(node) != -1