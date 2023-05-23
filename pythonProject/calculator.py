# Function for adding  numbers
def Addition(first, second):
    return first + second


# Function for Subtracting numbers
def Subtraction(first, second):
    return first - second


# Function for Multiplying number
def Multiplication(first, second):
    return first * second


# Function for Dividing numbers
def Divide(first, second):
    return first / second


def take_input():
    first = int(input("Please enter the first number:"))
    second = int(input("Please enter the second number:"))
    list_of_inputs = [first, second]
    return list_of_inputs


# choices for user
while True:
    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Enter your Requirement\n")
    print("+ for Addition of two number")
    print("- for Subtraction of two number")
    print("* for Multiplication of two number")
    print("/ for Divide of two number")
    print("0 to Exit\n")

    # User_Input is taken
    User_Input = input("Please enter your choice from + - * / 0 \n")

    # Operation takes place according to the user choice
    if User_Input == '+':
        inputs = take_input()
        print("Num1+Num2 :", Addition(inputs[0], inputs[1]))
        print("\n")

    elif User_Input == '-':
        inputs = take_input()
        print("Num1-Num2 :", Subtraction(inputs[0], inputs[1]))
        print("\n")

    elif User_Input == '*':
        inputs = take_input()
        print("Num1*Num2 :", Multiplication(inputs[0], inputs[1]))
        print("\n")

    elif User_Input == '/':
        inputs = take_input()
        print("Num1/Num2 :", Divide(inputs[0], inputs[1]))
        print("\n")

    elif User_Input == "0":
        exit(0)

    else:
        print("invalid choice")
