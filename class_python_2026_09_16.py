def myfun(x):
    x[1] = 7
    return None

# better version
def myfun(x):
    y = x.copy()
    y[1] = 7
    return y

x = [1.0, -2.7, 3.5, -5.1]

list(map(abs, x))

# functions are objects that we can treat like any other object
