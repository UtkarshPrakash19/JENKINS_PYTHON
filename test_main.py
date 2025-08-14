import main
import pytest

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

def test_multiply():
    """Test multiply function - NEW FEATURE"""
    assert main.multiply(2, 3) == 6
    assert main.multiply(0, 5) == 0
    assert main.multiply(4, 5) == 20

def test_divide():
    """Test divide function - FEATURE1 ONLY"""
    assert main.divide(10, 2) == 5.0
    assert main.divide(20, 4) == 5.0
    assert main.divide(9, 3) == 3.0
    
    # Test division by zero
    with pytest.raises(ValueError):
        main.divide(10, 0)

def test_main():
    """Test main function"""
    result1, result2, result3, result4 = main.main()
    assert result1 == 15  # 10 + 5
    assert result2 == 7   # 10 - 3
    assert result3 == 20  # 4 * 5
    assert result4 == 5.0 # 20 / 4

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_main()
    print("All tests passed!")
