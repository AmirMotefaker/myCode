# Code by @AmirMotefaker

# Working with files

# # Solution 1
# name = input('Enter your file name: ')

# open(f'{name}.txt', 'w') # w: write r: read

# # Output:
# # Enter your file name: info 
# # create file(info.txt)



# Solution 2
f = open('names.txt', 'w')

f.write('hello')


# Output:
# in file names.txt write hello
