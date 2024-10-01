t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    out = 0 
    for i, val in enumerate(a):
        if a[i] >= k:
            c += a[i]
        elif c > 0 and a[i] == 0:
            c -= 1
            out += 1
    print(out) 
