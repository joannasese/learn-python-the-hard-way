from sys import argv

script, input_file = argv

# function reads entire file ('f')
def print_all(f):
    print(f.read())

# goes to beginning of file
def rewind(f):
    f.seek(0)

# prints line number and content of that line
def print_a_line(line_count, f):
    print(line_count, f.readline())


# sets to open file (entered in terminal as command)
current_file = open(input_file)

print("First let's print the whole file:")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# current_line = 2
current_line += 1
print_a_line(current_line, current_file)

# current_line = 3
current_line += 1
print_a_line(current_line, current_file)
