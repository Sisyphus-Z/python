import re

# 1
# 1/2
# 1//3
# 1/2/3

f='f 1/2/3 11/22 111//333 1111/2222/3333'
v=1
vt=2
vn=3




def func1(parameter):
    s1=parameter.group("s1")
    s2 = parameter.group("s2")
    s3 = parameter.group("s3")
    print(s1, s2, s3)


    s1 = str(int(s1) - v)

    #s2可能性 '/' ‘/2'
    if s2 != '' and s2 !='/':
        s2 = s2.replace('/', '')
        s2 = str(int(s2) - vt)
        s2='/'+s2

    # s3可能性 '/' ‘/e' ''
    if s3 != '' and s3 !='/':
        s3 = s3.replace('/', '')
        s3 = str(int(s3) - vn)
        s3= '/'+s3
    print(s1,s2,s3)

    return ' {}{}{}\n'.format(s1,s2,s3)

ff=re.sub(' (?P<s1>\d*)(?P<s2>/?\d*)(?P<s3>/?\d*)',func1,f)

print(ff)