# Working with files is a common task for a programming language
# Python makes it easy. Let's look at an example:

myfile = open("/tmp/newfile.txt", "w")

# Open a file called newfile.txt in /tmp. If no file exists it will be
# created.
# The "w" is the mode, in this case "w" is for write. You could use "r"
# for read.
# There are various other modes we will cover them briefly later.

myfile.write("Here is my message.\n")
myfile.write("Here is my second message.")

# Write "Here is my message\n" to the file you opened. \n is a
# newline character.
# You need to add a \n every time you want to add a new line,
# otherwise everything will be on one line.

myfile.close()

# Since we opened the file, we need to close it when we're done with it.

# There are many different modes for opening a file in Python.
# Here are just a few useful ones:
# w - Allows you to write to a file only. If the file exists, it will
# be overwritten.
# r - Allows you to read the file only.
# r+ - Allows you to read and write to the file.
# w+ - Allows you to read and write to the file, but if the file
# already exists it will overwrite it.
# a - Allows you to append to the file
# (write to the end of an existing file)
# a+ - Allows you to append to the file, and read from the file.

myfile = open("/tmp/newfile.txt", "r")
filecontents = myfile.read()
print(filecontents)
myfile.close()

# Here we are reading the file we created previously.

# You can also use the 'with' syntax. It's better.
# Here is an example of reading a file line by line instead of all
# at once.

with open("/tmp/newfile.txt", "r") as myfile:
    for line in myfile:
        print(line)

# The major benefit of using 'with' is that it handles closing the
# file for you.
# We used a for loop to read the file line by line.

# CHALLENGE 1: Write a for loop that will create a file called
#              /tmp/cars.txt. There should be 50 lines of text in the
#              file. The first line should be "There are 0 cars"
#              and 1 car should be added every line. Until
#              the last line which should read "There are 49 cars"
def cars(intOne):
  return "There are " + str(intOne) + " cars\n"

with open("/tmp/cars.txt", "w") as myfile:
  for x in range(0, 50):
      myfile.write(cars(x))
    
# CHALLENGE 2: Open the file at /tmp/cars.txt and read the contents.
#              Print the contents to the screen.

with open("/tmp/cars.txt", "r") as myfile:
  print(myfile.read())