mark = int(input("Enter the mark: "))

# Check the grade based on the given conditions
if 90 <= mark <= 100:
    print("Grade: A")
elif 70 <= mark < 90:
    print("Grade: B")
elif 60 <= mark< 70:
    print("Grade: C")
else:
    print("Fail")
