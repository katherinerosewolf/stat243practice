message = ''
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + 'a'
    else:
        message = message + 'b'
print(message)

x = 1; y = 'foo'

xy = (x, y)
type(xy)
xy = x,y
type(xy)

xy
xy[1]

xy[1] = 3   # immutable!



def lr_slow(y, x):
    xtx = x.T @ x
    xty = x.T @ y
    inv = np.linalg.inv(xtx)
    return inv @ xty

## generate random observations and random matrix of predictors
n = 7000
y = np.random.normal(size = 7000)
x = np.random.normal(size = (7000,1000))

t0 = time.time()
regr = lr_slow(y, x)
t1 = time.time()
print(f"Execution time: {t1-t0} seconds.")

import cProfile
cProfile.run('lr_slow(y,x)')

import timeit

precode = '''
import numpy as np
x = np.random.normal(size = (7000,1000))
'''

code = '''
np.transpose(x)
'''

timeit.timeit(code, setup = precode, number = 1000)

precode_dot = '''
import numpy as np
x = np.random.normal(size = (7000,1000))
'''

code_dot = '''
x.T
'''

timeit.timeit(code_dot, setup = precode_dot, number = 1000)


# chi-squared test
import numpy as np

y = np.array([[5, 2, 4],
              [8, 3, 2], 
              [4, 6, 2]])

row_totals = y.sum(axis = 1, keepdims = True)
col_totals = y.sum(axis = 0, keepdims = True)

e = row_totals * col_totals / row_totals.sum()

squares = (y - e) ** 2 / e

chi_square = squares.sum()


# second line: 500^3