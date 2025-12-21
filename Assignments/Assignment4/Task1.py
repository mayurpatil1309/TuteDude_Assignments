
"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.


"""
try:
    with open("sample.txt","r") as f:
        content = f.readlines()
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")
else:
    print("Reading file content : ")
    for i in range(len(content)):
        print(f"Line{i+1} : {content[i].strip()}")


