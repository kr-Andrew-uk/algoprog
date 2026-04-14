from collections import deque

def min_knight_moves(n, start, end):
    row_moves = [2, 2, -2, -2, 1, 1, -1, -1]
    col_moves = [-1, 1, 1, -1, 2, -2, 2, -2]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (end[0], end[1]):
            return dist
        for i in range(8):
            nx = x + row_moves[i]
            ny = y + col_moves[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    return -1 

# дод завдання
def max_knight_moves(n, start):
    row_moves = [2, 2, -2, -2, 1, 1, -1, -1]
    col_moves = [-1, 1, 1, -1, 2, -2, 2, -2]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))
    max_dist = 0
    while queue:
        x, y, dist = queue.popleft()
        if dist > max_dist:
            max_dist = dist
        for i in range(8):
            nx = x + row_moves[i]
            ny = y + col_moves[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    return max_dist

def solve():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        n = int(lines[0].split('#')[0].strip())

        start_str = lines[1].split('#')[0].strip()
        start = tuple(map(int, start_str.split(',')))

        end_str = lines[2].split('#')[0].strip()
        end = tuple(map(int, end_str.split(',')))

        shortest_path = min_knight_moves(n, start, end)
        
        furthest_moves = max_knight_moves(n, start)

        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Найкоротший шлях: {shortest_path}\n")
            f.write(f"Найвіддаленіша клітинка(ходи): {furthest_moves}\n")
            
        print(f"Найкоротший шлях: {shortest_path}")
        print(f"Макс. ходів: {furthest_moves}")

    except FileNotFoundError:
        print("Файл input.txt не знайдено.")
    except Exception as e:
        print(f"Виникла помилка:  {e}")

if __name__ == "__main__":
    solve()