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

yog.color()

num399 = GrizzlyBear("Jackson Hole Grizzly 399", 35)
print(num399)

num399.color()

num399.num_people_killed

def lengthinator(x):
    if(isinstance(x, 'np.ndarray')):
        ...
    if(isinstance(x, 'np.ndarray')):
        ...


# yog = Bear(...) # init method

# yog() call something

class qClass:
    def __repr__(self):
        quit()

q = qClass()