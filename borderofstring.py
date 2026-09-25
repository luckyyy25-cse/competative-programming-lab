s = input().strip()
n = len(s)
for length in range(n - 1, 0, -1):
    if s[:length] == s[n - length:]:
        print(s[:length])
        break
