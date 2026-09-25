from math import gcd
A, B, T = map(int, input().split())
if T <= max(A, B) and T % gcd(A, B) == 0:
    print("YES")
else:
    print("NO")

