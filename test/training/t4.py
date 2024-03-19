'''This Python program accepts two lists of integers as input from the user and finds the common integers between them.'''
list1 = [int(number) for number in input("Enter first list of number: ").strip().split(" ")]
list2 = [int(number) for number in input("Enter second list of number: ").strip().split(" ")]
result = set(list1) & set(list2)
if (result):
    print(f"The common elements between two lists are: {list(result)}");
else:
    print("There are no common elements between two lists")
