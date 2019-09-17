# defining variable 'types_of_people' with value 10.
types_of_people = 10
# defining a format string x which uses variable types_of_people in it.
x = f"There are {types_of_people} types of people."

# variable binary with value binary
binary = "binary"
# variable do_not with value don't
do_not = "don't"
# defining a format string y which uses binary and do_not variable.
y = f"Those who know {binary} and those who {do_not}."

# printing x string
print(x)
# printing y string
print(y)

# printing formats string inside format string.
print(f"I said: {x}")
# again.
print(f"I also said: '{y}'")

# defining a bool variable 
hilarious = False
# defining a string that can take variable
joke_evaluation = "Isn't that joke so funny?! {}"

# making joke_evaluation take variable using .format()
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# strings can be concatenated using + operator.
print(w + e)