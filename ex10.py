tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# \n creates a linebreak
# \t creates an indentation
# \ before \ will allow '\' to show

# \apple
print("1. \\apple")
# apple'
print("2. apple\'")
# apple"
print("3. apple\"")
# apple with bell sound
print("4. apple\a")
# appl apple
print("5. apple\b apple")
print("6. apple\f")
print("7. apple\n")

print("8. apple\r")
print("9. apple\t")
print("10. apple\u6789")
# print("11. apple\U23456788")
print("12. apple\v")
print("13. apple\ooo")
