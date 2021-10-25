# --------------------settings-------------------
#
filename= '头发.obj'
#
# --------------------settings-------------------
import re


times=1

v=0
vn=0
vt=0

v_now=0
vn_now=0
vt_now=0

status=True
obj=[]

f=open(filename,'r')
ff_next=''

xxx=1

def func1(parameter):
    s1=parameter.group("s1")
    s2 = parameter.group("s2")
    s3 = parameter.group("s3")



    s1 = str(int(s1) - v+v_now)
    if int(s1) <=0:
        print('error:f 中有负数或0')

    #s2可能性 '/' ‘/2'
    if s2 != '' and s2 !='/':
        s2 = s2.replace('/', '')
        s2 = str(int(s2) - vt+vt_now)
        if int(s2) <= 0:
            print('error:f 中有负数或0')
        s2='/'+s2

    # s3可能性 '/' ‘/e' ''
    if s3 != '' and s3 !='/':
        s3 = s3.replace('/', '')
        s3 = str(int(s3) - vn+vn_now)
        if int(s3) <= 0:
            print('error:f 中有负数或0')
        s3= '/'+s3

    return ' {}{}{}'.format(s1,s2,s3)


while 1:
    # if xxx >100:
    #     break
    ff = ff_next
    ff_next=f.readline()




    if ff.find('v ')==0 :
        v_now+=1
        v+=1
    elif ff.find('vn')==0 :
        vn+=1
        vn_now += 1
    elif ff.find('vt')==0 :
        vt+=1
        vt_now+=1

    elif ff.find('f')==0 :


        ff=re.sub(' (?P<s1>\d*)(?P<s2>/?\d*)(?P<s3>/?\d*)',func1,ff)



    obj.append(ff)



    if ff.find('v ')!=0 and (ff_next.find('v ')==0 or ff_next=='') and ff !='':



        with open(filename.replace('.obj','')+str(times)+'.obj','w') as t:

            t.write("".join(obj))
            xxx += 1
        obj=[]

        v_now = 0
        vn_now = 0
        vt_now = 0
        times+=1

        if ff_next=='':
            break

        continue


f.close()