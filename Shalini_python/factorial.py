def get_valid_input():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Invalid input")

def calculate_factorial(num):
    if num < 0:
        print("factorial does not exist")
        return None
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

def print_output(num, factorial):
    if factorial is not None:
        print(f"The factorial of {num} is {factorial}")

def main():
    num = get_valid_input()
    factorial = calculate_factorial(num)
    print_output(num, factorial)

if __name__ == "__main__":
    main()
