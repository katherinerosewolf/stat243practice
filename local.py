gx = 7

def myfun(z):
    y = z*3
    print("local: ", locals())
    print("global: ", globals())

## Case 1
x = 3
def f2():
    print(x)

def f():
    x = 7
    f2()

f() # what will happen?

## Case 2
x = 3
def f2():
    print(x)

def f():
    x = 7
    f2()

x = 100
f() # what will happen?

## Case 3
x = 3
def f():
    def f2():
        print(x)        
    x = 7
    f2()

x = 100
f() # what will happen?

## Case 4
x = 3
def f():
    def f2():
        print(x)
    f2()

x = 100
f() # what will happen?


y = 100
def fun_constructor():
    y = 10
    def g(x):
        return x + y
    return g

## fun_constructor() creates functions
myfun = fun_constructor()
myfun(3)