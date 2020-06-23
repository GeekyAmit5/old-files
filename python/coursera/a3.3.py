score = float(input("Enter Score: "))
if score < 0 or score > 1:
    print("Please enter score between 0.0 and 1.0")
    quit()
if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'
print(grade)
