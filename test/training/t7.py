'''This Python program accepts an integer (n) and computes the value of n+nn+nnn.'''
number = input("Enter a number: ")
n1 , n2, n3 = int(number), int(number*2),int(number*3)
print(f"The result of '{n1} + {n2} + {n3}' is: {n1 + n2 + n3}")