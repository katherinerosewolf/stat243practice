def fastcount(xvar, yvar):
  naline = np.isnan(xvar) 
  naline[np.isnan(yvar)] = True 
  localx = xvar.copy() 
  localy = yvar.copy() 
  localx[naline] = 0 
  localy[naline] = 0 
  useline = ~naline 
  result = []   # create an empty list
  result[0] = useline
  ## We'll ignore the rest of the code.
 
  ## ....
 
  return result

# 1 no memory, pass by reference
# 2 line 1 uses memory
# 3 line 2 both yes and nos are right; list modified in place
## but new memory used because another call to isnan, which
## creates another boolean array, creates a temporary array
## in memory that gets used in indexing to modify elements
## in place in naline, even though not assigned
# 4 copies, yeah
# line 5, no new moeory, modifying in place
## not creating new boolean array
# 6, useline = ~naline, new object
# 7, new object, sure, a little memory, not not much
## returning object will not take up memory
## just list of references (but a little in terms
## the reference)
# no additional memory when returning it
## already created in memory, same object in memory
## as the one in local scope in the function


def myfun(val):
    if val <= 0:
        raise ValueError("`val` should be positive")

myfun(-3)


import os

def myfun(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
    except Exception as err:
        print(f"{err}\nCheck that the file `{filename}` can be found "\
              f"in the current path: `{os.getcwd()}`.")
        return None

    return(text.lower())


myfun('missing_file.txt')


import requests

def myfun(url):
    try:
        requests.get(url)
    except Exception as err:
        print(f"There was a problem accessing {url}. "\
              f"Perhaps it doesn't exist or the URL has a typo?")
        raise

myfun("http://missingurl_forsure.com")

dat = pd.read_csv(os.path.join('..', 'data', 'cpds.csv'))  


import polars
import time
t0 = time.time()
dat = pd.read_csv(os.path.join('..', 'data', 'airline.csv'))
t1 = time.time()
dat2 = polars.read_csv(os.path.join('..', 'data', 'airline.csv'), null_values = ['NA'])
t2 = time.time()
print(f"Timing for Pandas: {t1-t0}.")

print(f"Timing for Polars: {t2-t1}.")

# STARTING AT SECTION 3: ONLY READING

del mymod
try:           # Check if `mymod` is in scope.
    mymod.x
except Exception as error:
    print(error)


mydict = {'a': 3, 'b': 7}
mylist = [3, 5, 7]

mylist[1] = mydict
mylist

mydict['a'] = mylist


myList = [1, 3, 5, 9, 4, 7]
myList[2.0]    # What do you think is going to happen?
myList[2.73]   # What do you think is going to happen?

class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __str__(self):
          return f"A bear named '{self.name}' of age {self.age}."
      def color(self):
          return "unknown"

class GrizzlyBear(Bear):
      def __init__(self, name, age, num_people_killed = 0):
          super().__init__(name, age)
          self.num_people_killed = num_people_killed
      def color(self):  
          return "brown"

yog = Bear("Yogi the Bear", 23)
print(yog)


class Bear:
      count = 0
      def __init__(self, name, age):
          self.name = name
          self.age = age
          Bear.count += 1

yog = Bear("Yogi the Bear", 23)
yog.count


smokey = Bear("Smokey the Bear", 77)
smokey.count



yog.bizarre = 7
yog.bizarre

def foo(x):
    print(x)

foo.bizarre = 3
foo.bizarre

class QuitNow:
    def __repr__(self):
        raise SystemExit

q = QuitNow()

function = getattr(np, "mean")
function(np.array([1,2,3]))


def f(x):
    if x < 0:
        return -x**2
    else:
        res = x^2
        return x, res


f(-3)

f(3)

out1,out2 = f(3)