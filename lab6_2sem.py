from itertools import combinations


def solve(input_text):
    lines = input_text.strip().split('\n')
    N, B = map(int, lines[0].split())
    prefs_raw = list(''.join(lines[1].split()))

    employee_beers = []
    for i in range(N):
        liked = set()
        for j in range(B):
            if prefs_raw[i * B + j] == 'Y':
                liked.add(j)
        employee_beers.append(liked)

    for size in range(1, B + 1):
        for combo in combinations(range(B), size):
            selected = set(combo)
            if all(employee_beers[i] & selected for i in range(N)):
                return size


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    print(f"Кількість видів пива яку потрібно купити -", solve(data))