def solve():
    print("Введіть кількість листків, ширину та висоту")
    try:
        line = input().replace(',', ' ').split()
        if not line: return
        n, w, h = map(int, line)
    except ValueError:
        return

    min_len = max(w, h)
    max_len = max(w, h) * n
    ww_len = max_len
    iterations = 0

    while min_len <= max_len:

        iterations += 1
        mid_len = (min_len + max_len) // 2
        if mid_len == 0:
            min_len = mid_len + 1
            continue
            
        found_ww_len = (mid_len // w) * (mid_len // h)
        
        if found_ww_len >= n:
            ww_len = mid_len
            max_len = mid_len - 1
        else:
            min_len = mid_len + 1
            
    print(f"Мінімальний розмір дошки: {ww_len}")
    print(f"Кількість ітерацій (кроків пошуку): {iterations}")        
    print(ww_len)

solve()