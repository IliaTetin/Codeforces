s = input()
correct_out = 'hello'
cnt = 0
out = ''
for i in range(len(s)):
    if s[i] == correct_out[cnt]:
        out += s[i]
        cnt += 1
        if cnt >= len(correct_out):
            break
if out == correct_out:
    print("YES")
else:
    print("NO")
