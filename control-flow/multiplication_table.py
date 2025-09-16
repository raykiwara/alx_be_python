#script that asks the user to enter a number, then uses a for loop to print the multiplication table for that number from 1 to 10.

#prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

#multiplication table
for i in range(1, 11):
    mul = number * i
    print(f"{number} * {i} = {mul}")
