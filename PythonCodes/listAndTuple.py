'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a 
list and a tuple which contains every number.
'''
inp = input()
inp = [i.strip() for i in inp.split(',')]
print(inp) # Print list
print(tuple(inp)) # Print tuple
