t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    r = 0
    res = "YES"
    for cur in range(1, n):
        if a[cur] - a[l] == -1:
            l = cur
        elif a[cur] - a[r] == 1:
            r = cur
        else:
            res = "NO"
    print(res)
