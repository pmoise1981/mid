import logging
from calculator import Calculator, list_plugins

def repl():
    calculator = Calculator()
    print("Welcome to the CLI Calculator. Type 'exit' to quit.")
    
    while True:
        command = input("calc> ").strip().lower()
        if command == "exit":
            break
        elif command == "menu":
            print("Available commands: add, subtract, multiply, divide, plugins")
            print("Available plugins:", list_plugins())
            continue
        
        try:
            parts = command.split()
            if len(parts) < 3:
                raise ValueError("Invalid input. Use format: operation number number")
            
            operation = parts[0]
            args = [float(x) for x in parts[1:]]
            
            if operation == "add":
                print(calculator.add(*args))
            elif operation == "subtract":
                print(calculator.subtract(*args))
            elif operation == "multiply":
                print(calculator.multiply(*args))
            elif operation == "divide":
                print(calculator.divide(*args))
            elif operation in calculator.PLUGINS:
                print(calculator.execute_plugin(operation, *args))
            else:
                print("Unknown command")
        except Exception as e:
            logging.error(f"Error processing command: {e}")
            print("Error: Invalid input.")

if __name__ == "__main__":
    repl()

