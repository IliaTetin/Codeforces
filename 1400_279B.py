n, t = map(int, input().split())
a = list(map(int, input().split()))
l = 0
s = 0
res = 0 
for r in range(0, n):
    s += a[r]
    while s > t:
        s -= a[l]
        l += 1
    res = max(res, r-l+1)
print(res)
