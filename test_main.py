import main

def test_add():
    """Test add function"""
    assert main.add(2, 3) == 5
    assert main.add(0, 0) == 0
    assert main.add(-1, 1) == 0
    assert main.add(10, 5) == 15

def test_subtract():
    """Test subtract function"""
    assert main.subtract(5, 3) == 2
    assert main.subtract(0, 0) == 0
    assert main.subtract(1, 1) == 0
    assert main.subtract(10, 3) == 7

def test_main():
    """Test main function"""
    result1, result2 = main.main()
    assert result1 == 15  # 10 + 5
    assert result2 == 7   # 10 - 3

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_main()
    print("All tests passed!")
