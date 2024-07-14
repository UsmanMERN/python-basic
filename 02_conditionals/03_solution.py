input_marks = input("Enter your marks: \n")

marks_in_int = int(input_marks)

if marks_in_int > 100:
    print("Please Enter the correct marks")
    exit()
# input_marks
if marks_in_int >= 90:
    grade = "A"
elif marks_in_int >= 80:
    grade = "B"
elif marks_in_int >= 70:
    grade = "C"
elif marks_in_int >= 60:
    grade = "D"
else:
    grade = "F"

print("you scored grade", grade)

# input_marks = input("Enter your marks: \n")

# marks_in_int = int(input_marks)
# # input_marks
# if int(input_marks) >= 90:
#     print("you scored A grade")
# elif int(input_marks) >= 80:
#     print("you scored B grade")
# elif int(input_marks) >= 70:
#     print("you scored C grade")
# elif int(input_marks) >= 60:
#     print("you scored D grade")
# else:
#     print("you scored F grade")
