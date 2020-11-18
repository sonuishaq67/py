#!/usr/bin/python
val = input("Enter your value: ")
x = 0
for v in val:
    if not v.isalnum():
        print(v, end='')
        continue
    if x % 2 != 0:
        print(v.lower(), end='')
    else:
        print(v.upper(), end='')
    x = x+1
print()
