# Task1
## Student Marks Program
This is a simple Python program that stores student marks in a dictionary and allows the user to look up a student's mark by entering their name.

### Features
- Creates a dictionary where student names are keys and their marks are values.
- Accepts user input to search for a student.
- Retrieves and displays the corresponding marks.
- If the student’s name is not found, display an appropriate message.

### How the Program Works
1. A dictionary named `student_marks` stores student names as keys and their marks as values.
2. The user is prompted to enter a student's name.
3. The `.title()` to handle case-insensitive name input.
4. The program checks if the name exists in the dictionary:
   - If found, it prints the student's mark.
   - If not found, it prints `"Student not found"`.

### Example Output
#### if student found :
Enter the student's name: Alice  
Alice's mark : 85

#### if student not found
Enter the student's name: John  
Student not found


### Code Used
```python
student_marks = {'Alice':85, "Carl":90, "Bob":70, "David":80}
print(student_marks)

user = input("Enter the student's name: ").title()      #used title(), if user typed wrongly like ALICE,ALice,alice, then it will correct and give result
if user in student_marks:
    mark = student_marks[user]
    print(f"{user}'s mark : {mark}")
else:
    print("Student not found")
```





# Task2
## Python List Slicing and Reversing

This Python program describes how to:
- Create a list of numbers
- Extract the first five elements using list slicing
- Reverse the extracted elements

### Features
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list


###  How the Program Works
1. A list of numbers from 1 to 10 is created.
2. The first five elements are extracted using slicing (`[:5]`).
3. The extracted list is reversed using slicing (`[::-1]`).
4. The original list, extracted elements, and reversed list are printed.

### Example Output
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
Extracted first five elements: [1, 2, 3, 4, 5]  
Reversed extracted element: [5, 4, 3, 2, 1]


### Code Used
```python
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {original_list}")

first_five_elements = original_list[:5]
print(f"Extracted first five elements: {first_five_elements}")

reversed_list = first_five_elements[::-1]
print(f"Reversed extracted element: {reversed_list}")
```


