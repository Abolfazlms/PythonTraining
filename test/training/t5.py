''' This program accepts an input grade and converts it to a corresponding letter.'''
grade = int(input("Enter your grade: "));
match (grade):
    case grade if (grade >= 90) and (grade <= 100):
        letter_grade = 'A'
    case grade if (grade >= 80) and (grade < 90):
        letter_grade = 'B'
    case grade if (grade >= 70) and (grade < 80):
        letter_grade = 'C'
    case grade if (grade >= 60) and (grade <70):
        letter_grade = 'D'
    case grade if (grade < 70) :
        letter_grade = 'F'
    case _ :
        letter_grade = 'Unvalid Value'
print(f'Your letter grade is {letter_grade}');