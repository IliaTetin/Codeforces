n, k = map(int, input().split())
h = list(map(int, input().split()))
dif = max(h) - min(h)
out_cnt = 0
out = []

while True:
    curmaxind = h.index(max(h))
    curminind = h.index(min(h))
  
    if h[curmaxind] - h[curminind] <= 1:
        break
    out_cnt += 1
    h[curmaxind] -= 1
    h[curminind] += 1
    k -= 1
    out.append([curmaxind + 1, curminind + 1])
    dif = max(h) - min(h)        
    if k == 0:
        break
    if dif == 0:
        break
print(dif, out_cnt)
for i, val in enumerate(out):
    print(*val)
