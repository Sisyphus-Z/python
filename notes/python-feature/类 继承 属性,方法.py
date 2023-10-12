class Father():
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Son(Father):
    def __init__(self,x,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.x=x

a=Son(1,3,6)
print(a.x,a.name,a.age)

#-----------------------------------------------------------
print('------------------------------------------------')

class list1(list):
    def __str__(self):
        res=super().__str__()
        return res

b =list1('123456')
print(b)
