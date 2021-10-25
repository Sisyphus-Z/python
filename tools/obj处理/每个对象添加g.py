# --------------------settings-------------------
#
filename= 'a.obj'
times=1
#
# --------------------settings-------------------



ff_new=''

l=[]
with open(filename,'r') as f:
    while 1:
        ff=ff_new
        ff_new=f.readline()

        if (ff.find('vn ') ==0 or ff.find('vt ') ==0 or ff.find('v ') ==0) and (ff_new.find('f ') ==0 or ff_new.find('s ') ==0):
            times += 1
            ff=ff+'g {}\n'.format(times)

        l.append(ff)

        if ff_new == '':
            break



with open(filename+'处理后.obj','w') as f1:
    f1.write("".join(l))


print(times)