t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for k in range(n):
        s = input()
        for i in range(4):
            if s[i] == '#':
                lst.append(i+1)
    lst.reverse()
    print(*lst)    
