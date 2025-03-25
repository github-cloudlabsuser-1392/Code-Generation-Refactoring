class Calculator:
    def add(self, a, b):
        # Return the sum of a and b
        return a + b

    def subtract(self, a, b):
        # Return the difference of a and b
        return a - b

    def multiply(self, a, b):
        # Return the product of a and b
        return a * b

    def divide(self, a, b):
        # Return the quotient of a and b
        # Raise an error if b is zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    print("Add: ", calc.add(10, 5))
    print("Subtract: ", calc.subtract(10, 5))
    print("Multiply: ", calc.multiply(10, 5))
    print("Divide: ", calc.divide(10, 5))
