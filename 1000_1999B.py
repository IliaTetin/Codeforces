def game(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0


t = int(input())
for _ in range(t):
    a1, a2, a3, a4 = map(int, (input().split()))
    score = 0
    if game(a1, a3) + game(a2, a4) > 0:
        score += 1
    if game(a1, a4) + game(a2, a3) > 0:
        score += 1
    if game(a2, a3) + game(a1, a4) > 0:
        score += 1
    if game(a2, a4) + game(a1, a3) > 0:
        score += 1
    print(max(0, score))
