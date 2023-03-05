import numpy as np
from functools import reduce

# A 2D array
ara = np.array([(12,23,34,98),
                (90,78,52,10)])
                
# conversion of array to list
ray_to_list = ara.tolist()

# reducing 2D list to 1D
reduction_first = reduce(lambda x,y: x+y,ray_to_list)

# reducing pure list to single entity
reduction_second = reduce(lambda x,y: x+y-x, reduction_first)

# here we get 10 using exp x+y-x, which ultmately results in  last x of list; that is 10
print(reduction_second)

output: 10
