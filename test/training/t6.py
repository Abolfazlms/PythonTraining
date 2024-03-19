'''This Python program accepts a list of number and find the difference between the maximum and minimum values in it'''
list1 = [int(number) for number in input("Enter a list of integer value separated by spaces :").split()]
#methode 1
list1.sort()
maximum, minimum = list1[len(list1)-1], list1[0]

#method 2
# maximum = list1[0]
# minimum = list1[0]
# for i in range(len(list1)):    
#     if(list1[i] > maximum):
#         maximum = list1[i];
#     if(list1[i] < minimum):
#         minimum = list1[i];

#method3
# maximum = list1[0]
# minimum = list1[0]
# for i in list1:    
#     if(i > maximum):
#         maximum = i;
#     if(i < minimum):
#         minimum = i;

print(f'The difference between maximum {maximum} and minimum {minimum} values in the entered list is: {maximum - minimum}')