'''This Python program reads a CSV file of student data and calculates the average grade of female students.'''
from os.path import dirname, abspath, join
# Get the absolute path of the current directory
directory = dirname(abspath(__file__));
# Use the join() function to combine the absolute path of the current directory with the file name
fileName = join(directory,'students.csv')
with open(fileName,'r') as file:
    row = file.readlines();
female_s = 0;
female_s_grade = 0;
for s in row[1:]:
    value = s.split(',')
    gender = value[3];
    grade = int(value[4]);
    if(gender == "Female"):
        female_s += 1
        female_s_grade += grade
result = female_s_grade / female_s
print(f"The Average of {female_s} Female Student is: {result}")
