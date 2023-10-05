s = str(input())
a = str(input())
b = 0
s = s.replace(a, '1')
for i in range(0, len(s)):
    if s[i] == '1':
        b = b + 1
    else: break
print(b)
