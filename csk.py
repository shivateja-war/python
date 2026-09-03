student_name=input ("enter your name:")
student_marks=int(input("enter the  subject marks"))
if student_marks >= 90:
    print("Excellent")
elif student_marks >= "70":
   print("very good")
elif student_marks >= "50":
   print("pass")
elif student_marks <= "50":
   print("fail")
else :
   print("invalid")