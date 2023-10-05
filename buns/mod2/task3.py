a, b, c = map(int, input().split())
k = min(a, b, c)
m = max(a, b, c)
x = a + b + c - k - m
print(x)
