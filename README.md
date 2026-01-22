# TASK 3: Conditional Statements & Logical Flow (Python)

## Overview
This project implements a **Grade Calculator** using Python conditional statements.  
It demonstrates how decision-based business logic is written using `if-elif-else`, logical operators, nested conditions, input validation, and clean coding practices.

---

## Tools & Technologies
- Python 3
- VS Code
- Git & GitHub
- Windows OS

---

## Project Structure
Task_3/
├── grade_calculator.py
└── README.md

---

## Problem Statement
Create a program that:
- Takes marks input from the user
- Validates the input
- Calculates grades using conditional logic
- Displays appropriate messages for each grade

---

## Concepts Covered

### Conditional Statements
Uses `if-elif-else` to evaluate marks and assign grades.

### Logical Operators
- `and` → Used to define mark ranges  
- `or` → Used for input validation  

### Nested Conditions
Grading logic is applied only after validating marks, simulating real-world business rules.

### Input Validation
Ensures marks are between 0 and 100.

### Error Handling
Handles non-numeric input using `try-except`.

### Code Refactoring
Grading logic is written inside a function to improve readability and reuse.

---

## Grading Logic

| Marks Range | Grade | Remark |
|------------|-------|--------|
| 90 – 100 | A+ | Excellent |
| 80 – 89 | A | Very Good |
| 70 – 79 | B | Good |
| 60 – 69 | C | Average |
| 40 – 59 | D | Needs Improvement |
| Below 40 | F | Fail |

---

## How to Run
1. Clone the repository:
git clone https://github.com/rishitosh038/datatype_demo.git

2. Navigate to the folder:
cd Task_3

3. Run the program:
python grade_calculator.py

---

## Sample Input & Output

Input:
Enter your marks (0 - 100): 85

Output:
Grade: A  
Remark: Very good job!

---

## Learning Outcome
After completing this task, the learner will:
- Write decision-based logic using conditionals
- Apply logical operators correctly
- Implement nested business rules
- Validate user input safely
- Explain conditional flow clearly in interviews

---

## Note
This project is part of an internship training task focused on conditional logic and decision-making in Python.
