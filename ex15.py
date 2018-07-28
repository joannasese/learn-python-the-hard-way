from sys import argv

# set variables to argument
# you'll need to pass in variables in command line
script, filename = argv

# opens filename
txt = open(filename)

print(f"Here's your file {filename}:")
# prints out content of txt
print(txt.read())
# closes file
txt.close()

print("Type the filename again:")
# file_again set to user input,
# which will only work if the filename is entered exactly
file_again = input("> ")

# opens file (submitted through user input), set to variable 'txt_again'
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
