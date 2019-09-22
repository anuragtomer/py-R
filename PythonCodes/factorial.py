'''
Question 2:

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''

# Function to calculate Factorial of n
def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

# Get all the numbers for which factorial has to be calculated.
inp = input("Enter numbers:")

# Convert this string to list of single number string.
inp = inp.split(' ')

# get an empty list.
output = []
for i in inp:
    # i is string. int(i) would convert it into int.
    # fact returs int. That would be converted back to str and appended to output.
    output.append(str(fact(int(i))))

# join the strings in output by ','
print(', '.join(output))
