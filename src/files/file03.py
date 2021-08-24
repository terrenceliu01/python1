"""
with open block
"""

with open("hello.txt") as f:
    for line in f:
       print(line, end='')
    print("08: ", f.closed) # in with block, the file is not closed yet

print("10: ", f.closed) # out with block, the file automatically closed