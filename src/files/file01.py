"""
create a new file and write string to it
"""

file1 = open("data/hello.txt", "+w") # open for write from scratch
print("Hello world!\n", file=file1)

oceans = ("Pacific", 'Atlantic', 'Indian', 'Southen', 'Arctic')
for ocean in oceans:
    file1.write(ocean)
    file1.write("\n")

file1.close() # flush all content from buffer to disk

print("Done.")