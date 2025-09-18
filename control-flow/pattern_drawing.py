#script that prompts user to enter a positive integer, then use nested loops to print a square pattern made of asterisks (*)

#prompt for pattern size
size = int(input("Enter the size of the pattern: "))
length = size

#pattern
while size != 0:
    for i in range(0, length):
        print("*", end="")
    print()
    size -= 1
