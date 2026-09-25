s = input().strip()
seen = 0
duplicates = 0
result = []
for ch in s:
    bit = 1 << (ord(ch) - ord('a'))
    if seen & bit:
        if not (duplicates & bit):
            result.append(ch)
            duplicates |= bit
    else:
        seen |= bit
if result:
    print(*result)
else:
    print("No duplicates")
