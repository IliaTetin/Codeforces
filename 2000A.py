t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cnt = 0 
    if k == 1:
        print(n)
    else:
        while n > 0:
            cnt += n % k
            n //= k;
        print(cnt)
