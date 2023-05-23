"""
This is calculator program written in python using the class and objects.
"""
# declaring a Class


class Calculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
# Function for adding  numbers

    def addition(self):
        """
          Function for Adding numbers
        """
        return self.number_1+self.number_2
# Function for Subtracting numbers

    def subtraction(self):
        """
          Function for Subtraction numbers
        """
        return self.number_1-self.number_2
# Function for Multiplying numbers

    def multiplication(self):
        """
          Function for multiplying numbers
        """
        return self.number_1*self.number_2

    def divide(self):
        """
          Function for Dividing numbers
        """

        return self.number_1/self.number_2


def take_input():
    number_1 = int(input("Please enter the first number:"))
    number_2 = int(input("Please enter the second number:"))
    list_of_inputs = [number_1, number_2]
    return list_of_inputs


# choices for user
while True:
    print("----------------------------------")
    print("Enter the operation \n")
    print("+ for Addition of two number")
    print("- for Subtraction of two number")
    print("* for Multiplication of two number")
    print("/ for Divide of two number")
    print("0 to Exit\n")

    # User_Input is taken
    user_Input = input("Please enter your choice from + - * / 0 \n")
    # Operation takes place according to the user choice
    if user_Input == '+':
        inputs = take_input()
        obj = Calculator(inputs[0], inputs[1])
        print("number_1+number_2 :", obj.addition())
        print("\n")

    elif user_Input == '-':
        inputs = take_input()
        obj = Calculator(inputs[0], inputs[1])
        print("number_1-number_2 :", obj.subtraction())
        print("\n")

    elif user_Input == '*':
        inputs = take_input()
        obj = Calculator(inputs[0], inputs[1])
        print("number_1*number_2 :", obj.multiplication())
        print("\n")

    elif user_Input == '/':
        inputs = take_input()
        obj = Calculator(inputs[0], inputs[1])
        print("number_1/number_2 :", obj.divide())
        print("\n")

    elif user_Input == "0":
        break

    else:
        print("invalid choice")
