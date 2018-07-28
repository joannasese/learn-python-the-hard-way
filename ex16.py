from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do what that, hit RETURN.")
input("?")

print("Opening the file...")
# "w" mode creates the file if it does not exist,
# and empties it if it does.
# "r+" opens a file for reading and writing
target = open(filename, 'w')

# clears the file
# doesn't seem to be needed if in 'w' mode,
# since file gets emptied if the file exists
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
all_lines = f"{line1}\n{line2}\n{line3}"

print("I'm going to write these to the file.")
target.write(all_lines)

print("And finally, we close it.")
target.close()
