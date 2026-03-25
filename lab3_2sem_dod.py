import os


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    def build_regular_from_postorder(cls, postorder: list):
        if not postorder:
            return None
        
        root_val = postorder[-1]
        root = cls(root_val)
        
        remaining = postorder[:-1]
        
        if remaining:
            mid = len(remaining) // 2
            root.left = cls.build_regular_from_postorder(remaining[:mid])
            root.right = cls.build_regular_from_postorder(remaining[mid:])
            
        return root

    def _get_height(self) -> int:
        left_height = self.left._get_height() if self.left else 0
        if left_height == -1:
            return -1
        right_height = self.right._get_height() if self.right else 0
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def is_tree_balanced(self) -> bool:
        return self._get_height() != -1

    def print_tree(self):
        def display_aux(n):
            if n is None:
                return [], 0, 0, 0
            if n.right is None and n.left is None:
                line = str(n.value)
                return [line], len(line), 1, len(line) // 2

            left, n_w, n_h, n_m = display_aux(n.left)
            right, m_w, m_h, m_m = display_aux(n.right)
            s = str(n.value)
            u = len(s)

            first_line = (n_m + 1) * " " + (n_w - n_m - 1) * "_" + s + m_m * "_" + (m_w - m_m) * " "
            second_line = n_m * " " + "/" + (n_w - n_m - 1 + u + m_m) * " " + "\\" + (m_w - m_m - 1) * " "

            if n_h < m_h:
                left += [n_w * " "] * (m_h - n_h)
            elif m_h < n_h:
                right += [m_w * " "] * (n_h - m_h)

            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
            return lines, n_w + m_w + u, max(n_h, m_h) + 2, n_w + u // 2

        lines, *_ = display_aux(self)
        for line in lines:
            print(line)

    def print_top_view(self):
        canvas = {}

        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        depth = get_depth(self)

        initial_dy = 2 ** max(1, depth - 1)
        dx = 6 

        def draw(node, x, y, dy, is_left_side, is_root=False):
            if not node:
                return
            
            canvas[(x, y)] = str(node.value)

            if is_root:
                if node.left:
                    for i in range(2, dx): canvas[(x - i, y)] = "-"
                    draw(node.left, x - dx, y, dy, True, False)
                if node.right:
                    for i in range(2, dx): canvas[(x + i, y)] = "-"
                    draw(node.right, x + dx, y, dy, False, False)
            else:
                next_dy = max(1, dy // 2)
                if is_left_side:
                    if node.left:
                        canvas[(x - dx // 2, y - dy // 2)] = "\\"
                        draw(node.left, x - dx, y - dy, next_dy, True, False)
                    if node.right:
                        canvas[(x - dx // 2, y + dy // 2)] = "/"
                        draw(node.right, x - dx, y + dy, next_dy, True, False)
                else:
                    if node.left:
                        canvas[(x + dx // 2, y - dy // 2)] = "/"
                        draw(node.left, x + dx, y - dy, next_dy, False, False)
                    if node.right:
                        canvas[(x + dx // 2, y + dy // 2)] = "\\"
                        draw(node.right, x + dx, y + dy, next_dy, False, False)

        draw(self, 0, 0, initial_dy, True, True)

        if not canvas:
            return

        min_y = min(y for x, y in canvas.keys())
        max_y = max(y for x, y in canvas.keys())
        min_x = min(x for x, y in canvas.keys())
        max_x = max(x for x, y in canvas.keys())

        for y in range(min_y, max_y + 1):
            row_items = {x: val for (x, cy), val in canvas.items() if cy == y}
            if not row_items:
                continue

            line_chars = []
            curr_x = min_x
            while curr_x <= max_x:
                if curr_x in row_items:
                    val = row_items[curr_x]
                    line_chars.append(val)
                    curr_x += len(val)
                else:
                    line_chars.append(" ")
                    curr_x += 1
            print("".join(line_chars).rstrip())


def read_data_from_file(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().replace("[", " ").replace("]", " ").replace(",", " ")
            return [int(item) for item in content.split()]
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено")
        return []
    except ValueError:
        print("У файлі містяться некоректні дані")
        return []


if __name__ == "__main__":
    file_name = "input.txt"

    data = read_data_from_file(file_name)

    if data:
        print(f"Вхідний post order масив: {data}")

        root = BinaryTree.build_regular_from_postorder(data)

        if root:
            print("Базове дерево")
            root.print_tree()

            print("Вигляд зверху")
            root.print_top_view()

            is_balanced = root.is_tree_balanced()
            print(f"Дерево збалансоване? {'Так' if is_balanced else 'Ні'}")
    else:
        print("Будь ласка, створіть файл input.txt і додайте туди масив.")