"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""
data = input("Enter text to write to the file: ")
file_name = "output.txt"
with open(file_name, "w") as file:
    file.write(data+"\n")
    print("Data successfully written to output.txt\n")

additional_data = input("Enter text to append : ")
with open(file_name, "a+") as file:
    file.write(additional_data)
    print("Data successfully appended\n")
    file.seek(0)       # to get pointer at the beginning, if not used, then when we are going to read the file it returns empty string
    content = file.read()
    print(f"Final content of output.txt: \n{content}")


