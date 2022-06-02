# Code by @AmirMotefaker

# Split a List Into Evenly Sized Chunks

# Solution 1 - Using yield
# def split(list_a, chunk_size):

#   for i in range(0, len(list_a), chunk_size):
#     yield list_a[i:i + chunk_size]

# chunk_size = 2
# my_list = [1,2,3,4,5,6,7,8,9]
# print(list(split(my_list, chunk_size)))


# Solution 2
# chunk_size = 2
# list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
# print(list_chunked)


# Solution 3 - Using numpy
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9]
print(np.array_split(my_list, 5))
