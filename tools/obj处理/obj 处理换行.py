# --------------------settings-------------------
#
filename='全部.obj'
#
# --------------------settings-------------------




#  windows python 貌似自动会把\n转换成 \r\n

l=[]
with open(filename,'r') as f:
    while 1:
        ff=f.readline()

        l.append(ff)

        if ff == '':
            break

with open(filename+'处理后.obj','w') as f1:
    f1.write("".join(l))
