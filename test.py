try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a number")
    n = int(input("Enter a number: "))
else:
    print(n)