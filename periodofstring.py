s = input().strip()
n = len(s)
for p in range(1, n + 1):
    if n % p == 0:
        if s == s[:p] * (n // p):
            print(p)
            break
