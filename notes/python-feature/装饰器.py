def wrapper1(func):
    def c(*args,**kwargs):
        print('套上了装饰器外壳')
        return func(*args,**kwargs)
    return c

@wrapper1
def a(x,y):
    return x+y

print(a(3,4))


def wrapper_params(*args0,**kwargs0):
    def wrapper2(func):
        def c(*args,**kwargs):
            print('装饰器的参数是{}{}'.format(args0,kwargs0))
            return func(*args,**kwargs)
        return c
    return wrapper2

@wrapper_params(1,2,3,v=1,z=2)
def b(x,y):
    return x*y

print(b(8,9))
