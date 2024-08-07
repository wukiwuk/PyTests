def main():
    n = get_number()
    print(f"Your number is {n}")

def get_number():
    while True:
        try:
            n = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number")
        else:
            return n


main()