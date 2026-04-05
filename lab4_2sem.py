class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.priority >= current.priority:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.priority >= parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self._insert_fixup(new_node)

    def extract_max(self):
        if self.root == self.NIL:
            return None

        z = self.root
        while z.left != self.NIL:
            z = z.left

        max_val_and_priority = (z.value, z.priority)

        y = z
        y_original_color = y.color
        x = z.right

        self._transplant(z, z.right)

        if y_original_color == "BLACK":
            self._delete_fixup(x)

        return max_val_and_priority

    def peek(self):
        if self.root == self.NIL:
            return None

        z = self.root
        while z.left != self.NIL:
            z = z.left
            
        return (z.value, z.priority)


    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _insert_fixup(self, k):
        while k.parent is not None and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def _delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

if __name__ == "__main__":
    pq = RedBlackPriorityQueue()
    
    print("Вставляємо елементи: (Значення, Пріоритет)")
    items_to_insert = [("Task A", 5), ("Task B", 6), ("Task C", 4), ("Task D", 8), ("Task E", 9), ("Task F", 7), ("Task G", 2), ("Task K", 1), ("Task K", 3)]
    for val, prio in items_to_insert:
        print(f"Вставка: {val} (Пріоритет: {prio})")
        pq.insert(val, prio)

    print(f"Перегляд найвищого: {pq.peek()}")

    while True:
        max_item = pq.extract_max()
        if max_item is None:
            break
        print(f"Значення = {max_item[0]}, Пріоритет = {max_item[1]}")