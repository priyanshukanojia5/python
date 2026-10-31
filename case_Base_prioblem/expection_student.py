try:
    # Convert user input into an integer
    marks = int(input("Enter marks: "))

    # Validate the marks
    if marks < 0 or marks > 700:
        raise ValueError("Marks must be between 0 and 700")

    subjects = int(input("Enter number of subjects: "))

    # Prevent division by zero
    if subjects <= 0:
        raise ZeroDivisionError("Subjects must be greater than zero")

    print("Average:", marks / subjects)

except ValueError as e:
    # Handles invalid numbers and invalid marks
    print("Invalid input:", e)

except ZeroDivisionError as e:
    # Handles zero or negative subject count
    print("Calculation error:", e)