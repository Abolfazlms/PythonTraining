'''This Python program accepts an integer as input from the user to draw Khayyam Pascal's triangle.'''
depth = int(input("Enter a number: "))
triangle = [[1]]
for i in range(1,depth):
    row = [1]
    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j]);
    row.append(1)
    triangle.append(row);
for row in triangle:
    print(" " * (depth - len(row)), end = "")
    for number in row:
        print(f"{number} ",end = "")
    print()
