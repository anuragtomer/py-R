from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

'''
1st method:

in_file = open(from_file) # You opened it. Later you need to close this one.
indata = in_file.read()

2nd method:
indata = open(from_file).read()
'''
print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output files exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# You need to skip closing in_file because you closed it immediately after opening it
# if you used method 2 of reading text.
in_file.close()
