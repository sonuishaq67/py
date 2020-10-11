val = input("Enter your value: ")
x = 0
for v in val:
    if x % 2 != 0:
        print(v.lower(),end='')
    else:
        print(v.upper(),end='')
    x = x+1
print()
