types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Formatters work by putting in one or more replacement fields or placeholders
# — defined by a pair of curly braces {} —
# into a string and calling the str.format() method.
# ex: print("Sammy has {} balloons.".format(5))
# output: Sammy has 5 balloons.
hilarious = False
joke_evaluation = "Isnt' that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
