from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Another way of writing into the target file:
'''
1 way:
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

2nd way:
target.write(f"{line1}\n{line2}\n{line3}")
'''
print("And finally, we close it.")
target.close()

# Additional exercise.
# Lets read it back.

print("We are going to read back what you wrote.")
print("What was the file name again? ")
filename = input("> ")

print(f"Oh ya.. Correct. It was {filename}. Lets see what it has got in it.")
target = open(filename, 'r')
print(target.read())
target.close()