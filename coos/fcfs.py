r=[53,42,14,12,78,176,48]
h=54
m=0
for i in r:
    m+=abs(h-1)
    h=i
print(m)