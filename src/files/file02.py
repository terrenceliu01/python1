"""
read existing file and add new line in the same file
"""

def readFile(filename):
    file1 = open(filename) # open file by default is read mode
    text = file1.read()
    file1.close()
    return text

def write2file(filename, line):
    file1 = open(filename, "a") # open file for append
    file1.write(line + "\n")
    file1.close()

if __name__ == '__main__':
    text = readFile("hello.txt")
    print(text)

    write2file("hello.txt", "this is a new line append to existing file.")