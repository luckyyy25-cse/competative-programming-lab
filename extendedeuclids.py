import math
import sys
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    D, x0, y0 = extended_gcd(A, B)
    step_x = B // D
    step_y = A // D
    k_center_x = -x0 / step_x
    k_center_y = y0 / step_y
    candidates_k = set()
    for center in (k_center_x, k_center_y):
        k_base = math.floor(center)
        for offset in range(-2, 3):
            candidates_k.add(k_base + offset)
    best_pair = None
    min_sum = float('inf')
    for k in candidates_k:
        x = x0 + k * step_x
        y = y0 - k * step_y
        abs_sum = abs(x) + abs(y)
        if abs_sum < min_sum:
            min_sum = abs_sum
            best_pair = (x, y)
        elif abs_sum == min_sum:
            if x < best_pair[0]:
                best_pair = (x, y)
    print(f"{best_pair[0]} {best_pair[1]} {D}")
if __name__ == '__main__':
    solve()
