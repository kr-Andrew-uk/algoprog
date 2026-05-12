import math

def solve(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split()
    
    if not input_data:
        return
    
    w = int(input_data[0])
    heights = [int(x) for x in input_data[1:]]
    n = len(heights)
    
    if n <= 1:
        print("0.00")
        return

    dp_1 = 0.0
    dp_h = 0.0

    for i in range(1, n):
        prev_h = heights[i-1]
        curr_h = heights[i]

        dist_1_1 = w
        dist_h_1 = math.hypot(w, prev_h - 1)
        dist_1_h = math.hypot(w, 1 - curr_h)
        dist_h_h = math.hypot(w, prev_h - curr_h)

        new_dp_1 = max(dp_1 + dist_1_1, dp_h + dist_h_1)
        new_dp_h = max(dp_1 + dist_1_h, dp_h + dist_h_h)

        dp_1 = new_dp_1
        dp_h = new_dp_h

    max_length = max(dp_1, dp_h)
    
    print(f"{max_length:.2f}")

if __name__ == "__main__":
    solve("input.txt")