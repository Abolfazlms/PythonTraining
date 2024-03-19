'''This Python program reads student data from a CSV file and calculates several statistics.'''
from os.path import dirname, abspath, join
# Get the absolute path of the current directory
directory = dirname(abspath(__file__));
# Use the join() function to combine the absolute path of the current directory with the file name
fileName = join(directory,'students.csv')
with open(fileName,'r') as file:
    next(file)  # row[1:]
    # row = file.readlines();
    data_dict = {};
    
    youngest_student = float('inf');
    oldest_student = 0;
    highest_grade = 0;
    lowest_grade = float('inf')    
    for line in file :
        value = line.strip().split(',')
        name = value[1];
        age = int(value[2]);
        grade = int(value[4]);

        if(age < youngest_student):
            youngest_student = age;
        if(age > oldest_student):
            oldest_student = age;
        if grade > highest_grade:
            highest_grade = grade;
        if grade < lowest_grade:
            lowest_grade = grade;
    
    data_dict["youngest_student"] = youngest_student;
    data_dict["oldest_age"] = oldest_student;
    data_dict["highest_grade"] = highest_grade;
    data_dict["lowest_grade"] = lowest_grade;
print(data_dict)

