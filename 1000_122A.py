n = int(input())
lucky = [4,7,47,74,477,744]
flag = False
for i in range(len(lucky)):
    if n % lucky[i] == 0:
        print('YES')
        flag = True
        break
if not flag:
    print('NO')
