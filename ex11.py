# end=' ' prevents a line break, replace it with a ' '
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()
print("What is the proper number of bowling balls?", end=' ')
balls = input()

print(f"""
So, you're {age} old, {height} tall and {weight} heavy.
You have {balls} bowling balls.
""")
