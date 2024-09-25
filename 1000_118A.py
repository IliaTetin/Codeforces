s = input()
out = ''
letters = ["A", "a", "O", "o", "Y", "y", "E", "e", "U", "u", "I", "i"]
for i in range(len(s)):
    if s[i] not in letters:
        out += '.'
        out += s[i].lower()
print(out)        


