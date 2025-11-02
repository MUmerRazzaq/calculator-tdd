from typing import Any
import pytest
import sys
from io import StringIO
from unittest.mock import patch
from src.calculator import add, subtract, multiply, divide


def test_divide_by_zero_raises_error() -> None:
    """Test that dividing by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    
    with pytest.raises(ZeroDivisionError):
        divide(-5, 0)
    
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)


def test_divide_by_zero_message() -> None:
    """Test that dividing by zero provides appropriate error message."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)


def test_operations_with_extremely_large_numbers() -> None:
    """Test calculator operations with extremely large numbers to check for overflow."""
    # Now that we have a max value of 10**100, operations with numbers like 10**308 will cause overflow
    large_num = 10**308  # This is much larger than our 10**100 limit
    
    # Addition with large numbers should raise OverflowError
    with pytest.raises(OverflowError):
        add(large_num, large_num)
    
    # Subtraction with large numbers should raise OverflowError
    with pytest.raises(OverflowError):
        subtract(large_num, large_num // 2)
    
    # Multiplication with large numbers should raise OverflowError
    with pytest.raises(OverflowError):
        multiply(large_num, 2)
    
    # Division with large numbers should raise OverflowError
    with pytest.raises(OverflowError):
        divide(large_num, 2)


def test_operations_with_very_small_numbers() -> None:
    """Test calculator operations with very small numbers to check for precision issues."""
    small_num = 1e-308  # Very small positive number
    
    # Addition with small numbers
    result1 = add(small_num, small_num)
    assert result1 == 2 * small_num
    
    # Subtraction with small numbers
    result2 = subtract(small_num, small_num / 2)
    assert result2 == small_num / 2
    
    # Multiplication with small numbers
    result3 = multiply(small_num, 2)
    assert result3 == 2 * small_num
    
    # Division with small numbers
    result4 = divide(small_num, 2)
    assert result4 == small_num / 2


def test_operations_with_infinity() -> None:
    """Test calculator operations involving infinity."""
    import math
    
    inf = float('inf')
    
    # All operations with infinity should now raise OverflowError due to our range checking
    with pytest.raises(OverflowError):
        add(inf, 5)
    
    with pytest.raises(OverflowError):
        subtract(inf, 5)
    
    with pytest.raises(OverflowError):
        multiply(inf, 5)
    
    with pytest.raises(OverflowError):
        divide(inf, 5)
    
    # Also test operations that result in infinity
    with pytest.raises(OverflowError):
        multiply(10**200, 10**200)  # Would result in infinity
    
    with pytest.raises(OverflowError):
        add(10**200, 10**200)  # Would result in very large number


def test_operations_with_nan() -> None:
    """Test calculator operations with NaN (Not a Number)."""
    import math
    
    nan = float('nan')
    
    # All operations with NaN should result in NaN
    assert math.isnan(add(nan, 5))
    assert math.isnan(subtract(nan, 5))
    assert math.isnan(multiply(nan, 5))
    assert math.isnan(divide(nan, 5))
    
    # Operations with NaN as second operand
    assert math.isnan(add(5, nan))
    assert math.isnan(subtract(5, nan))
    assert math.isnan(multiply(5, nan))
    assert math.isnan(divide(5, nan))


def test_calculator_with_invalid_types() -> None:
    """Test calculator functions with invalid input types."""
    with pytest.raises(TypeError):
        add("string", 5)
    
    with pytest.raises(TypeError):
        subtract(5, "string")
    
    with pytest.raises(TypeError):
        multiply([1, 2], 5)
    
    with pytest.raises(TypeError):
        divide(5, {"key": "value"})


def test_overflow_error_handling() -> None:
    """Test calculator behavior with overflow conditions."""
    import math
    
    # Test multiplication that should result in overflow error
    with pytest.raises(OverflowError):
        multiply(10**200, 10**200)
    
    # Test addition that should result in overflow error
    with pytest.raises(OverflowError):
        add(10**101, 10**101)
    
    # Test subtraction that should result in overflow error
    with pytest.raises(OverflowError):
        subtract(10**101, -10**101)
    
    # Test division that should result in overflow error
    with pytest.raises(OverflowError):
        divide(10**101, 10**(-101))


def test_result_too_large_error() -> None:
    """Test calculator behavior with results that are too large."""
    import math
    
    # Very large multiplication that might cause issues
    try:
        result = multiply(10**310, 10**310)  # This will likely result in infinity
        # If it doesn't raise an error, check if it's infinity
        assert math.isinf(result)
    except OverflowError:
        # This is also acceptable behavior for overflow
        pass


def test_very_small_number_precision() -> None:
    """Test operations with very small numbers to check for precision issues."""
    import math
    
    # Very small number that's still within our range
    tiny = 1e-10  # Well within our range limit
    
    # Addition with small numbers should work fine
    result = add(tiny, tiny)
    assert result >= 0  # Result should be non-negative
    assert isinstance(result, (int, float))
    
    # Small numbers within range should be fine
    result2 = multiply(tiny, 1e5)
    assert isinstance(result2, (int, float))
    
    # However, multiplying very small by very large might exceed range
    with pytest.raises(OverflowError):
        multiply(1e-100, 1e200)  # Result would be 1e100, at the limit


def test_cli_division_by_zero_error_handling() -> None:
    """Test CLI error handling for division by zero."""
    with patch('sys.argv', ['calculator', 'divide', '10', '0']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Cannot divide by zero" in error_output


def test_cli_invalid_operation_error_handling() -> None:
    """Test CLI error handling for invalid operations."""
    with patch('sys.argv', ['calculator', 'invalid_op', '5', '3']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Unknown operation" in error_output
        assert "add, subtract, multiply, divide" in error_output


def test_cli_invalid_number_format_error_handling() -> None:
    """Test CLI error handling for invalid number formats."""
    with patch('sys.argv', ['calculator', 'add', 'abc', '5']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Invalid number format" in error_output


def test_cli_insufficient_arguments_error_handling() -> None:
    """Test CLI error handling for insufficient arguments."""
    with patch('sys.argv', ['calculator', 'add', '5']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Usage:" in error_output


def test_cli_too_many_arguments_error_handling() -> None:
    """Test CLI error handling for too many arguments."""
    with patch('sys.argv', ['calculator', 'add', '5', '3', '1']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Usage:" in error_output


def test_cli_help_command() -> None:
    """Test CLI help command."""
    with patch('sys.argv', ['calculator', '--help']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with pytest.raises(SystemExit):
                main()
        output = captured_output.getvalue()
        assert "Usage:" in output
        assert "add" in output
        assert "subtract" in output
        assert "multiply" in output
        assert "divide" in output


def test_cli_negative_number_handling() -> None:
    """Test CLI handling of negative numbers."""
    with patch('sys.argv', ['calculator', 'add', '-5', '3']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        assert float(output) == -2.0


def test_cli_float_precision_handling() -> None:
    """Test CLI handling of floating point precision."""
    with patch('sys.argv', ['calculator', 'add', '0.1', '0.2']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        # Handle potential floating point precision issues
        assert abs(float(output) - 0.3) < 1e-10