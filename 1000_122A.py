n = int(input())
lucky = [4,7,44,47,74,77, 447,474, 477, 744,747,777]
flag = False
for i in range(len(lucky)):
    if n % lucky[i] == 0:
        print('YES')
        flag = True
        break
if not flag:
    print('NO')
