s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.isalnum() or ch == " ":
        result += ch
print("String after removing special characters:")
print(result)
