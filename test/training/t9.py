# This Python program accepts a string from user and checks if it is a palindrome or not.
text = input('Enter a text: ').strip().lower()
reverse = text[::-1]
if(reverse == text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} isn't a palindrome.")