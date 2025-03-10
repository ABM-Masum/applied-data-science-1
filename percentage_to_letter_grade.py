grade = input("Please give your grade in percentages (0-100):")

if grade.isdigit() and 0 <= int(grade) <= 100:
    grade = int(grade)
    if grade >= 90:
        print("Your letter grade is A")
    elif grade >= 80:
        print("Your letter grade is B")
    elif grade >= 70:
        print("Your letter grade is C")
    elif grade >= 60:
        print("Your letter grade is D")
    else:
        print("Your letter grade is F")
else:
    print("Please input a digit between 0 and 100.")
