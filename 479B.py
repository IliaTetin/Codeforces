n, k = map(int, input().split())
h = list(map(int, input().split()))

maxdif = max(h) - min(h)
out_cnt = 0
out = []
while maxdif != 0 or k != 0:
    curmax = max(h)
    curmaxind = h.index(max(h))
    curmin = min(h)
    curminind = h.index(min(h))
    out_cnt += 1
    out.append([curmaxind + 1, curminind + 1])

    h[curmaxind] -= 1
    h[curminind] += 1
    k -= 1
    newdif = maxdif - (max(h) - min(h))
    if newdif == 0:
        #out_cnt -= 1
        #out.pop()
        break
    else:
        maxdif = max(h) - min(h)
print(maxdif, out_cnt)
for i, val in enumerate(out):
    print(*val)

