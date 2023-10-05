s = map(int, input().replace(' ',''))
s = sorted(s)
g = False 
for i in range(0, len(s)):
    if s.count(i) > 1:
        g = True
print(g)
