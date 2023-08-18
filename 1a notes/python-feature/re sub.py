import re

a='bbb.111,222,aaa,ee,12,33'

def func0(parameter):
    temp =parameter.group("n2")
    print(temp)
    return '被替换'

aa=re.sub('(?P<n1>\d+),(?P<n2>\d+)',func0,a)

print(aa)