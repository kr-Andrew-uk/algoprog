import os


def build_prefix_function(needle: str) -> list[int]:
    n = len(needle)
    prefix = [0] * n
    k = 0

    for i in range(1, n):
        while k > 0 and needle[k] != needle[i]:
            k = prefix[k - 1]
        if needle[k] == needle[i]:
            k += 1
        prefix[i] = k

    return prefix


def kmp_search(haystack: str, needle: str) -> list[int]:
    if not isinstance(haystack, str) or not isinstance(needle, str):
        raise TypeError("Обидва аргументи повинні бути рядками.")

    if not needle or not haystack:
        return []

    n = len(haystack)
    m = len(needle)

    if m > n:
        return []

    prefix = build_prefix_function(needle)
    indices = []
    q = 0

    for i in range(n):
        while q > 0 and needle[q] != haystack[i]:
            q = prefix[q - 1]
        if needle[q] == haystack[i]:
            q += 1
        if q == m:
            indices.append(i - m + 1)
            q = prefix[q - 1]

    return indices


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    haystack = lines[0]
    needle = lines[1]

    print(f"Текст:  {haystack}")
    print(f"Пошук:  {needle}")

    result = kmp_search(haystack, needle)

    if result:
        print(f"\nЗнайдено входжень: {len(result)}")
        print(f"Індекси: {result}")
        for idx in result:
            print(f"  [{idx}] -> «{haystack[idx:idx + len(needle)]}»")
    else:
        print("\nВходжень не знайдено.")