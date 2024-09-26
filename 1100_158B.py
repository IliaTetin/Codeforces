n = int(input())
s = list(map(int, input().split()))
t1, t2, t3, t4 = 0, 0, 0, 0


for i, val in enumerate(s):
    if val == 4:
        t4 += 1
    elif val == 3:
        t3 += 1
        while t1 != 0 and t3 !=0:
            t4 += 1
            t3 -= 1
            t1 -= 1

    elif val == 2:
        t2 += 1
        if t2 == 2:
            t4 += 1
            t2 -= 2
    else:
        t1 += 1

while t3 != 0 and t1 != 0:
    t3 -= 1
    t1 -= 1
    t4 += 1
    
while t2 > 0 and t1 > 0:
    t3 += 1
    t2 -= 1
    t1 -= 1
    while t3 != 0 and t1 != 0:
        t3 -= 1
        t1 -= 1
        t4 += 1

temp = 0
for i in range(t1):
    temp += 1
    t1 -= 1
    if temp == 4:
        t4 += 1
        temp = 0

if temp == 3 and t1 == 1:
    t4 += 1
    t1 -= 1
    temp = 0
elif temp == 2 and t1 == 1:
    t3 += 1
    t1 -= 1
    temp = 0
elif temp == 1 and t1 == 1:
    t2 += 1
    t1 -= 1
    temp = 0
else:
    if temp == 4:
        t4 += 1
    elif temp == 3:
        t3 += 1
    elif temp == 2:
        t2 += 1
    else:
        t1 += temp

#print(t4,t3,t2,t1)
print(t4+t3+t2+t1)