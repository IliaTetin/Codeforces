a = int(input())
b = int(input())
c = int(input())

vars = [a*(b+c), a+b+c, a*b*c, (a+b)*c, a+b*c, a*b+c]
print(max(vars))