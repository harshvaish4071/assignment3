#grading of a student
grade=int((input('please enter your grade point:\n')))
if grade==10:
    print('your grade is A+ and your performance is Outstanding')
elif grade==9:
    print('your grade is A and your performance is Excellent')
elif grade==8:
    print('your grade is B+ and your performance is Very Good')
elif grade==7:
    print('your grade is B and your performance is Good')
elif grade==6:
    print('your grade is C+ and your performance is Average')
elif grade==5:
    print('your grade is C and your performance is Below Average')
elif grade==4:
    print('your grade is D and your performance is Poor')
else:
    print("Error:sorry this grade dosn't exist")