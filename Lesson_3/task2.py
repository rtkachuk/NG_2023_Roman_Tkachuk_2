file = open("test.txt", "a") # w - write, r - read, x - create, a - add to the end
file.write("Hello")
file.close()

# More interesting file write :3

with open("test2.txt", "a") as f:
    f.write ("Testing")
print ("Goodbye :3")

# Let's read multiple-lined file!

with open("test3.txt", "r") as f:
    for line in f.readlines():
        print (line, end="")