from itertools import combinations


def parse_input(text):
    lines = text.strip().split('\n')
    N, B = map(int, lines[0].split())
    prefs_raw = list(''.join(lines[1].split()))
    prices = list(map(int, lines[2].split()))

    employee_beers = []
    for i in range(N):
        liked = set()
        for j in range(B):
            if prefs_raw[i * B + j] == 'Y':
                liked.add(j)
        employee_beers.append(liked)

    return N, B, employee_beers, prices


def covers_all(combo_set, employee_beers):
    return all(employee_beers[i] & combo_set for i in range(len(employee_beers)))


def calc_total_cost(combo_set, employee_beers, prices):
    bottles = {j: 0 for j in combo_set}
    total = 0
    for liked in employee_beers:
        available = liked & combo_set
        cheapest = min(available, key=lambda j: prices[j])
        bottles[cheapest] += 1
        total += prices[cheapest]
    return total, bottles


def find_min_count(B, employee_beers, prices):
    best_combo = None
    best_cost = float('inf')
    for size in range(1, B + 1):
        for combo in combinations(range(B), size):
            s = set(combo)
            if covers_all(s, employee_beers):
                cost, _ = calc_total_cost(s, employee_beers, prices)
                if best_combo is None:
                    best_combo = combo
                    best_cost = cost
                elif cost < best_cost:
                    best_cost = cost
                    best_combo = combo
        if best_combo is not None:
            return best_combo, best_cost
    return None, 0


def find_min_cost(B, employee_beers, prices):
    best_combo = None
    best_cost = float('inf')
    for size in range(1, B + 1):
        for combo in combinations(range(B), size):
            s = set(combo)
            if covers_all(s, employee_beers):
                cost, _ = calc_total_cost(s, employee_beers, prices)
                if cost < best_cost:
                    best_cost = cost
                    best_combo = combo
    return best_combo, best_cost


def format_result(combo, bottles, prices, N):
    lines = []
    for j in combo:
        n = bottles[j]
        lines.append(f"Пиво {j+1}: {n} пляшок × {prices[j]} грн = {n * prices[j]} грн")
    return lines


def solve_extra(input_text):
    N, B, employee_beers, prices = parse_input(input_text)

    min_count_combo, count_cost = find_min_count(B, employee_beers, prices)
    min_cost_combo, min_cost    = find_min_cost(B, employee_beers, prices)

    _, count_bottles = calc_total_cost(set(min_count_combo), employee_beers, prices)
    _, cost_bottles  = calc_total_cost(set(min_cost_combo),  employee_beers, prices)


    print(f"Працівників: {N}, Сортів пива: {B}")
    print(f"Ціна за пляшку: { {f'Пиво {j+1}': prices[j] for j in range(B)} }")

    print(f"\n  Мінімальна КІЛЬКІСТЬ сортів: {len(min_count_combo)}")
    for line in format_result(min_count_combo, count_bottles, prices, N):
        print(f"   {line}")
    print(f"   Разом: {count_cost} грн ({N} пляшок)")

    print(f"\n  Мінімальна ВАРТІСТЬ закупки: {min_cost} грн")
    for line in format_result(min_cost_combo, cost_bottles, prices, N):
        print(f"   {line}")
    print(f"   Разом: {min_cost} грн ({N} пляшок, {len(min_cost_combo)} сортів)")

    if set(min_count_combo) == set(min_cost_combo):
        print("\n Обидва підходи дають однаковий результат!")
    else:
        saved = count_cost - min_cost
        extra = len(min_cost_combo) - len(min_count_combo)
        print(f"\n  Купуючи за мінімальною вартістю:")
        print(f"   Економія: {saved} грн")
        if extra > 0:
            print(f"   Проте доведеться взяти на {extra} сорт(и) більше")

    return len(min_count_combo), min_cost

if __name__ == '__main__':
    with open('input_extra.txt', 'r') as f:
        data = f.read()
    solve_extra(data)