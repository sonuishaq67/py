#!/usr/bin/python
test_str = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpulukvwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(test_str)
print(str(all_freq))

test_str_decoded = ""

for x in test_str:
    bruh = (ord(x) - 7 - 97) % 26
    bruh = bruh + 97
    test_str_decoded = test_str_decoded + chr(bruh)

print(str(test_str_decoded))
