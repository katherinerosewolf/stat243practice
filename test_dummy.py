import pytest
import numpy as np

import dummy

def test_numeric():
    assert dummy.add_one(3) == 4

# This test will fail.
def test_numpy_array():
    assert np.all(np.equal(dummy.add_one(np.array([3,4])), np.array([4,5])))

def test_bad_input():
    with pytest.raises(TypeError):
        dummy.add_one('hello')

def test_warning():
    with pytest.warns(UserWarning, match='complex'):
        dummy.add_one(1+3j)

        import warnings

def mysqrt(x):
    if isinstance(x, str):
        raise TypeError(f"What is the square root of '{x}'?")
    if isinstance(x, (float, int)):
        if x < 0:
            warnings.warn("Input value is negative.", UserWarning)
            return float('nan')   # Avoid complex number result.
        else:
            return x**0.5
    else:
        raise ValueError(f"Cannot take the square root of {x}")


mysqrt(3.1)

import numpy as np
import pandas as pd
import random
import statsmodels.api

np.random.seed(2)
n_cats = 30
n = 80
y = np.random.normal(size=n)
x = np.random.normal(size=n)
cats = [np.random.randint(0, n_cats-1) for _ in range(n)]
data = pd.DataFrame({'y': y, 'x': x, 'cats': cats})

params = np.full((n_cats, 2), np.nan)
for i in range(n_cats):
    sub = data[data['cats'] == i]
    try:
        model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
        fit = model.fit()
        params[i, :] = fit.params.values
    except Exception as error:
        print(f"Regression cannot be fit for stratum {i}.")

print(params)




import numpy as np
mat = np.array([[1, 2], [3, 4]])
np.sum(mat, axis=0)         # This sums columns, as desired

row_subset = 1
mat2 = mat[row_subset, :]
np.sum(mat2, axis=0)        # This sums the elements, not the columns. 


if len(mat2.shape) != 2:    # Fix dimensionality.
    mat2 = mat2.reshape(1, -1)


np.sum(mat2, axis=0)   

text = "Here's my number: 919-543-3300."
m = re.search("\\d+", text)
m

m.group()

m.start()

m.end()

m.span()

re.search("\\d+", "a93b")

tmp = "Harry said, \"Hi\""
print(tmp)   # This prints out without a newline -- this is hard to show in rendered doc.

tmp = ["azar", "foo", "hello\tthere\n"]
print(tmp[2])

re.search("[\tZ]", tmp[2])   # Search for a tab or a 'Z'.

## Search for characters that are not 'z'
## (using ^ as regular expression syntax)
re.search("[^z]", "zero")


## Show results for various input strings:

import re
for st in ["a^2", "93", "zzz", "zit", "azar"]:
    print(st + ":\t", re.search("[^z]", st))


for st in ["a^2", "93", "zzz", "zit", "azar"]:
    print(st + ":\t", re.search("[\\^z]", st))


    

## Search for exactly three characters
## (using . as regular expression syntax)
for st in ["abc", "1234", "def"]:
    print(st + ":\t", re.search("^.{3}$", st))

    

## Search for a period (as a regular character)
for st in ["3.9", "27", "4.2"]:
    print(st + ":\t", re.search("\\.", st)) 


    ## Use and search for an actual backslash
tmp = "something \\ other\n"
print(tmp) 

re.search("\\\\", tmp)

try:
    re.search("\\", tmp)
except Exception as error:
    print(error)



class 

class InstaQuit:
    def __repr__(self):
        raise SystemExit

q = InstaQuit()



## Use and search for an actual backslash
tmp = "something \\ other\n"
print(tmp) 
## Search for an actual backslash
re.search(r"\\", tmp)

import os
import pandas as pd
file_path = os.path.join('..', 'data', 'RTADataSub.csv')
chunksize = 50 # Obviously this would be much larger in any real application.

with pd.read_csv(file_path, chunksize = chunksize) as reader:
     for chunk in reader:
         # Manipulate the lines and store the key stuff.
         print(f'Read {len(chunk)} rows.')


import io

file_path = os.path.join('..', 'data', 'precip.txt')
with open(file_path, 'r') as file:
     text = file.read()

stringIOtext = io.StringIO(text)
df = pd.read_fwf(stringIOtext, header = None, widths = [3,8,4,2,4,2])

dat = pd.read_csv('../data/cpds.csv')

## good: will work on Windows
dat = pd.read_csv('../data/cpds.csv')
## bad: won't work on Mac or Linux
dat = pd.read_csv('..\data\cpds.csv')  

## good: operating-system independent
dat = pd.read_csv(os.path.join('..', 'data', 'cpds.csv'))  