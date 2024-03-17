student = input("Enter the name of the student")
Maths = float(input('Enter the first marks'))
English= float(input('Enter the second marks'))
Physics = float(input('Enter the third marks'))
Chemistry = float(input('Enter the fourth marks'))
Computer = float(input('Enter the fifth marks'))

average = (Maths+English+Physics+Chemistry+Computer)/(5)
if average >= 70 and average <= 100:
    grade = "A"
elif average >= 60 and average <= 69:
    grade = "B"
elif average >= 50 and average <= 59:
    grade = "C"
elif average >= 43 and average <= 49:
    grade = "D"
elif average >= 40 and average <= 42:
    grade = "E"
else:
    grade = "F"
print("student name" +student)
print("Makrs is", Maths, "", English, "", Physics, "", Chemistry,"", Computer)
print("Average:", average)
print("Grade", grade)
          
             
              
