n = int(input())
sx, sy, sz = 0, 0, 0
for i in range(n):
    x,y,z = map(int, input().split())
    sx += x
    sy += y
    sz += z
if sx == 0 & sy == 0 & sz == 0:
    print('YES')
else:
    print('NO')
