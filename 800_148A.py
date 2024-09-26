k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
res = 0

for i in range(1, d+1):
    flag = False
    if i >= k: 
        if i % k == 0:
            flag = True
    if not flag:
        if i >= l:
            if i % l == 0:
                flag = True
    if not flag:
        if i >= m:
            if i % m == 0:
                flag = True
    if not flag:
        if i >= n:
            if i % n == 0:
                flag = True
    if flag:
        res += 1
print(res)
