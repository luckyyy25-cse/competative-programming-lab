i, j = map(int, input().split())
original_i = i
original_j = j
if i > j:
    i, j = j, i
max_cycle = 0
for n in range(i, j + 1):
    x = n
    cycle_length = 1
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        cycle_length += 1
    max_cycle = max(max_cycle, cycle_length)
print(original_i, original_j, max_cycle)
