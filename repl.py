import cmd
from commands import Calculator

class CalculatorREPL(cmd.Cmd):
    intro = "Welcome to the Calculator REPL. Type 'help' to list commands."
    prompt = "calc> "
    
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
    
    def do_add(self, arg):
        "Add two numbers: add 3 5"
        try:
            a, b = map(float, arg.split())
            result = self.calculator.add(a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Provide two numeric values.")
    
    def do_subtract(self, arg):
        "Subtract two numbers: subtract 10 4"
        try:
            a, b = map(float, arg.split())
            result = self.calculator.subtract(a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Provide two numeric values.")
    
    def do_multiply(self, arg):
        "Multiply two numbers: multiply 6 7"
        try:
            a, b = map(float, arg.split())
            result = self.calculator.multiply(a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Provide two numeric values.")
    
    def do_divide(self, arg):
        "Divide two numbers: divide 8 2"
        try:
            a, b = map(float, arg.split())
            result = self.calculator.divide(a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Provide two numeric values.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    
    def do_mean(self, arg):
        "Calculate the mean of a list of numbers: mean 1 2 3 4 5"
        try:
            numbers = list(map(float, arg.split()))
            result = self.calculator.mean(numbers)
            print(f"Mean: {result}")
        except ValueError:
            print("Error: Provide numeric values.")
    
    def do_median(self, arg):
        "Calculate the median of a list of numbers: median 1 2 3 4 5"
        try:
            numbers = list(map(float, arg.split()))
            result = self.calculator.median(numbers)
            print(f"Median: {result}")
        except ValueError:
            print("Error: Provide numeric values.")
    
    def do_mode(self, arg):
        "Calculate the mode of a list of numbers: mode 1 1 2 3 4"
        try:
            numbers = list(map(float, arg.split()))
            result = self.calculator.mode(numbers)
            print(f"Mode: {result}")
        except ValueError:
            print("Error: Provide numeric values.")
        except StatisticsError:
            print("Error: No unique mode found.")
    
    def do_quit(self, arg):
        "Exit the calculator REPL."
        print("Goodbye!")
        return True

if __name__ == "__main__":
    CalculatorREPL().cmdloop()

