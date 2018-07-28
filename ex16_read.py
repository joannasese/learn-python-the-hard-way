from sys import argv

script, filename = argv

txt = open(filename)

print("Here's what you said:")
print(txt.read())
