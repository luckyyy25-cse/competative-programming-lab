s = input().strip()
p = input().strip()
i = 0
j = 0
star = -1
match = 0
while i < len(s):
    if j < len(p) and (p[j] == s[i] or p[j] == '?'):
        i += 1
        j += 1
    elif j < len(p) and p[j] == '*':
        star = j
        match = i
        j += 1
    elif star != -1:
        j = star + 1
        match += 1
        i = match
    # No match
    else:
        print(0)
        break
else:
    # Skip remaining *
    while j < len(p) and p[j] == '*':
        j += 1

    if j == len(p):
        print(1)
    else:
        print(0)
