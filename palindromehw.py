s = input("Enter a string: ")
pal = True
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        pal = False
        break
    i += 1
    j -= 1
if pal:
    print("Palindrome")
else:
    print("Not Palindrome")
