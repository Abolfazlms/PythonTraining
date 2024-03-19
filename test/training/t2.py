''' This Python program accepts an integer (n) and then find all of the numbers from 1–n that are divisible by 8'''
number = int(input("Enter a number: "))
result = [num for num in range(1,number) if (num % 8 == 0)]
print(f"All of the numbers from 1-{number} that are divisible by 8 is : {result}")