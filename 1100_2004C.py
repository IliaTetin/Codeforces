t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))
    cost.sort(reverse=True)
    out = 0
    for i in range(0, n, 2):
        out += cost[i]
        if i + 1 < n:
            if k > 0:
                diff = min(cost[i] - cost[i+1], k)
                cost[i+1] += diff
                k -= diff
            out -= cost[i+1]
    print(out)