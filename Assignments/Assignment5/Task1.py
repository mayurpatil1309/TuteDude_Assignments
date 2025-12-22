
"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.


"""

student_marks = {'Alice':85, "Carl":90, "Bob":70, "David":80}
print(student_marks)

user = input("Enter the student's name: ").title()      #used title(), if user typed wrongly like ALICE,ALice,alice, then it will correct and give result
if user in student_marks:
    mark = student_marks[user]
    print(f"{user}'s mark : {mark}")
else:
    print("Student not found")