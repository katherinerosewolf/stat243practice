import psutil

# Get memory information
memory_info = psutil.Process().memory_info()

# Print the memory usage
print("Memory usage:", memory_info.rss/10**6, " MB.")


# Let's turn that into a function for later use:
def mem_used():
    print("Memory usage:", psutil.Process().memory_info().rss/10**6, " MB.")

import numpy as np
nums = np.array([1,2,3,4])
mystring = 'hat'
inner_list = ['hat','cat']
