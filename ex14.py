from sys import argv

script, user_name, pet = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

# print(f"Where is your habitat {user_name}?")
# below prints similar format, but requires repeating \n each time.
lives = input(f"Where is your habitat {user_name}?\n> ")

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Remember to walk {pet} today.
""")
