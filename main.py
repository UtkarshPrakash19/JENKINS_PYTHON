def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def main():
    """Main function"""
    print("Basic Python App - Main Branch")
    result1 = add(10, 5)
    result2 = subtract(10, 3)
    
    print(f"10 + 5 = {result1}")
    print(f"10 - 3 = {result2}")
    
    return result1, result2

if __name__ == "__main__":
    main()
