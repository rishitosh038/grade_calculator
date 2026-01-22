# -------------------------------
# Grade Calculator Program
# -------------------------------

def calculate_grade(marks):
    """
    Determines grade based on marks using conditional logic
    """

    # Validate marks range
    if marks < 0 or marks > 100:
        return "Invalid marks! Marks must be between 0 and 100."

    # Nested conditions for grading rules
    if marks >= 90:
        grade = "A+"
        message = "Excellent performance!"
    elif marks >= 80 and marks < 90:
        grade = "A"
        message = "Very good job!"
    elif marks >= 70 and marks < 80:
        grade = "B"
        message = "Good performance."
    elif marks >= 60 and marks < 70:
        grade = "C"
        message = "Average performance."
    elif marks >= 40 and marks < 60:
        grade = "D"
        message = "Needs improvement."
    else:
        grade = "F"
        message = "Fail. Better luck next time."

    return f"Grade: {grade}\nRemark: {message}"


# -------------------------------
# Main Program Execution
# -------------------------------

try:
    # Taking user input
    user_marks = float(input("Enter your marks (0 - 100): "))

    # Calculate and display grade
    result = calculate_grade(user_marks)
    print("\nResult:")
    print(result)

except ValueError:
    print("Invalid input! Please enter numeric marks only.")

# -------------------------------
# End of Program
# -------------------------------
