# Author: Wilfred Majaliwa
# Date: 2023-07-01
# Description: Exception Handling & File Handling
# Session: Afternoon
# Github: https://github.com/techymaj/recess-2.git
# Assignment: 5

# An Exception is an error that happens during execution of a program.
# When that error occurs, Python generate an Exception that can be handled
# Which avoids your program to crash.

# Three types of errors can occur in a Python program:
# 1. Syntax errors
# 2. Logical errors
# 3. Runtime errors


# Exception Handling With Try & Except
import traceback


print("#" * 80)
print("Exception Handling With Try & Except")
number = input("Enter a number: ")
try:  
    # This code will run if the input is a number
    number = int(number)
    print(number)
except ValueError as err:
    # This code will run if the input is not a number
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")
print("#" * 80)
print("\n")

# Exception Handling using raise
print("#" * 80)
print("Exception Handling using raise")
number = input("Enter a number: ")
try:
    number = int(number)
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    print(number)
except ValueError as err:
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")
print("#" * 80)
print("\n")

# Exception Handling using assert
print("#" * 80)
print("Exception Handling using assert")
number = input("Enter a number: ")
try:
    number = int(number)
    # The assert keyword lets you test if a condition in your code returns True, 
    # if not, the program will raise an AssertionError.
    assert number >= 0 
    # OR assert number >= 0, "Negative numbers are not allowed" 
    # prints "Negative numbers are not allowed" if the number is negative and the traceback
    print(number)
except AssertionError as err:
    print("Invalid input. Please enter a number")
    # traceback.print_exc() prints the traceback of the error
    # import traceback
    traceback.print_exc()
    # Standard assert statement doesn't put anything into the AssertionError, 
    # it's the traceback that matters
    print(f"Error: {err}")
print("#" * 80)
print("\n")

# Exception Handling using else
print("#" * 80)
print("Exception Handling using else")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
else:
    # This code will run if the input is a number
    print(number)
print("#" * 80)
print("\n")

# Exception Handling using finally
print("#" * 80)
print("Exception Handling using finally")
number = input("Enter a number: ")
try:
    number = int(number)
    # This syntaxt will print the traceback of the error if the input is negative
    # And the AssertionError will be raised as "Negative numbers are not allowed"
    assert number >= 0, "Negative numbers are not allowed"
finally:
    # This code will always run
    print(number)
    print("This code will always run")
print("#" * 80)
print("\n")


# Multiple except clauses
print("#" * 80)
print("Multiple except clauses")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
except ValueError:
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")


# Exceptions as a tuple in a single except clause
print("#" * 80)
print("Exceptions as a tuple in a single except clause")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except (AssertionError, ValueError):
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")



# File Handling 
# Python has several functions for creating, reading, updating, and deleting files.
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# create a file called demofile.txt with the contents "This is a demo file"
print("#" * 80)
print("create a file called demofile.txt with the contents 'This is a demo file'")
f = open("demofile.txt", "w")
f.write("This is a demo file")
f.close()
print("#" * 80)
print("\n")

# To open a file for reading it is enough to specify the name of the file:
print("#" * 80)
print("To open a file for reading it is enough to specify the name of the file:")
f = open("demofile.txt")
print(f.read())
print("#" * 80)
print("\n")

# Read Only Parts of the File
print("#" * 80)
print("Read Only Parts of the File")
f = open("demofile.txt", "r")
print(f.read(5))
print("#" * 80)
print("\n")

# Read Lines
print("#" * 80)
print("Read Lines")
f = open("demofile.txt", "r")
print(f.readline())
print("#" * 80)
print("\n")

# Close Files
print("#" * 80)
print("Close Files")
f = open("demofile.txt", "r")
print(f.readline())
f.close()
print("#" * 80)
print("\n")

# Write to an Existing File
print("#" * 80)
print("Write to an Existing File")
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
print("#" * 80)
print("\n")

# Overwrite the content
print("#" * 80)
print("Overwrite the content")
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
print("\n")

#open and read the file after the overwriting:
print("#" * 80)
print("open and read the file after the overwriting:")
f = open("demofile.txt", "r")
print(f.read())
print("#" * 80)
print("\n")

# Create a New File
print("#" * 80)
print("Create a New File")
open("myfile.txt", "x")
print("#" * 80)
print("\n")

# Delete a File
print("#" * 80)
print("Delete a File")
import os
os.remove("myfile.txt")
print("#" * 80)
print("\n")

# Check if File exist
print("#" * 80)
print("Check if File exist")
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
print("#" * 80)
print("\n")

# create a folder called myfolder
print("#" * 80)
print("create a folder called myfolder")
import os
os.mkdir("myfolder")
print("#" * 80)
print("\n")

# Delete Folder
print("#" * 80)
print("Delete Folder")
import os
os.rmdir("myfolder")
print("#" * 80)
print("\n")

# create a file called demofile.txt
print("#" * 80)
print("create a file called demofile.txt")
open("demofile.txt", "x")
print("#" * 80)
print("\n")

# Read a file using with
print("#" * 80)
print("Read a file using with")
with open("demofile.txt", "r") as f:
    print(f.read())
print("#" * 80)
print("\n")

# Write to a file using with
print("#" * 80)
print("Write to a file using with")
with open("demofile.txt", "w") as f:
    f.write("Hello World")
print("#" * 80)
print("\n")

# Read and Write to a file using with
print("#" * 80)
print("Read and Write to a file using with")
with open("demofile.txt", "r+") as f:
    print(f.read())
    f.write("Hello World")
print("#" * 80)
print("\n")


# Using a main function, 
# create a program that will create a file myfile.txt, 
# add the content "Hello World" to the file, and then print the content of the file.
# The file should be created in the same directory as the program and use exception handling.
print("#" * 80)
print("Using a main function, create a program that will create a file myfile.txt, add the content Hello World to the file, and then print the content of the file. The file should be created in the same directory as the program and use exception handling.")
def main():
    try:
        with open("myfile.txt", "x") as f:
            f.write("Hello World")
            f.close()
    except FileExistsError:
        print("The file already exists")
    with open("myfile.txt", "r") as f:
        print(f.read())
        f.close()


if __name__ == "__main__":
    main()
print("#" * 80)
print("\n")


