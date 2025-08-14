def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers - NEW FEATURE"""
    return a * b

def divide(a, b):
    """Divide two numbers - FEATURE1 ONLY"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Main function"""
    print("Basic Python App - Feature1 Branch")
    result1 = add(10, 5)
    result2 = subtract(10, 3)
    result3 = multiply(4, 5)
    result4 = divide(20, 4)
    
    print(f"10 + 5 = {result1}")
    print(f"10 - 3 = {result2}")
    print(f"4 * 5 = {result3}")
    print(f"20 / 4 = {result4}")
    
    return result1, result2, result3, result4

if __name__ == "__main__":
    main()
