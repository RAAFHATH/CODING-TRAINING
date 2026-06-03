s = input("Enter a string: ")
print("Duplicate Characters:")
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count > 1:
        duplicate = False
        for k in range(i):
            if s[i] == s[k]:
                duplicate = True
                break
        if not duplicate:
            print(s[i])

