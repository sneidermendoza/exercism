from operator import index
from re import M


l = []
s = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
d = l + s
c = 5
# print (c in d)
# # r = (s[0] + s[-1]) / 2
# # print(r)
# a = int(len(s) / 2)
# print(s[a])
m =(s[-1] * 2)
l.append(m)
s[-1:] = l
print(s)