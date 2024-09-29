def f(a,b,c):
    return (c-a) + (b-c)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    best_c = a
    val = f(a, b, best_c)

    for c in range(a, b+1):
        cur_val = f(a,b,c)
        if cur_val < val:
            best_c = c
            val = cur_val
    print(f(a,b,best_c))
