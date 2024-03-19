'''This Python program accepts a text string from the user and counts the vowels in it.'''
text = input("Enter a text : "); 
vowels = ['a','e','i','o','u'];
counter = 0;
for letter in text:
    if(letter.lower() in vowels):
        counter += 1;
print(f"There are {counter} vowels in the text string.")