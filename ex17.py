from sys import argv
from os.path import exists

script, from_file, to_file = argv

# not a crucial line
# print(f"Copying from {from_file} to {to_file}")

# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read();

print(f"""
The input file is {len(indata)} bytes long.
Does the output file exist? {exists(to_file)}
Hit RETURN to continue, CTRL-C to abort.
""")
input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
out_file = open(to_file, 'w').write(indata)

print("Alright, all done.")

# out_file.close()
# not necessary to run 'in_file.close()
# when 'indata = open(from_file).read()' is used,
# because is should already be closed once that line runs
# in_file.close()
