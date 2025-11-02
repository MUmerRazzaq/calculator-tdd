from typing import Any
import pytest
import sys
from io import StringIO
from unittest.mock import patch
from src.calculator import add, subtract, multiply, divide


def test_cli_add_positive_integers() -> None:
    """Test CLI addition with positive integers."""
    with patch('sys.argv', ['calculator', 'add', '5', '3']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        # Since CLI processes numbers as floats, result will be displayed as float
        assert float(output) == add(5.0, 3.0)


def test_cli_subtract_positive_integers() -> None:
    """Test CLI subtraction with positive integers."""
    with patch('sys.argv', ['calculator', 'subtract', '10', '4']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        # Since CLI processes numbers as floats, result will be displayed as float
        assert float(output) == subtract(10.0, 4.0)


def test_cli_multiply_positive_integers() -> None:
    """Test CLI multiplication with positive integers."""
    with patch('sys.argv', ['calculator', 'multiply', '6', '7']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        # Since CLI processes numbers as floats, result will be displayed as float
        assert float(output) == multiply(6.0, 7.0)


def test_cli_divide_positive_integers() -> None:
    """Test CLI division with positive integers."""
    with patch('sys.argv', ['calculator', 'divide', '10', '2']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        assert output == str(divide(10, 2))


def test_cli_operations_with_floats() -> None:
    """Test CLI operations with floating point numbers."""
    # Addition
    with patch('sys.argv', ['calculator', 'add', '2.5', '3.7']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        assert float(output) == add(2.5, 3.7)
    
    # Division
    with patch('sys.argv', ['calculator', 'divide', '5.5', '2.0']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        assert float(output) == divide(5.5, 2.0)


def test_cli_operations_with_negative_numbers() -> None:
    """Test CLI operations with negative numbers."""
    # Addition with negative
    with patch('sys.argv', ['calculator', 'add', '-5', '3']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        # Since CLI processes numbers as floats, result will be displayed as float
        assert float(output) == add(-5.0, 3.0)
    
    # Multiplication with negatives
    with patch('sys.argv', ['calculator', 'multiply', '-4', '-3']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        output = captured_output.getvalue().strip()
        # Since CLI processes numbers as floats, result will be displayed as float
        assert float(output) == multiply(-4.0, -3.0)


def test_cli_division_by_zero() -> None:
    """Test CLI division by zero - should raise error."""
    with patch('sys.argv', ['calculator', 'divide', '10', '0']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Cannot divide by zero" in error_output


def test_cli_invalid_operation() -> None:
    """Test CLI with invalid operation - should show error."""
    with patch('sys.argv', ['calculator', 'invalid_op', '5', '3']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Unknown operation" in error_output


def test_cli_invalid_number_format() -> None:
    """Test CLI with invalid number format - should show error."""
    with patch('sys.argv', ['calculator', 'add', 'abc', '5']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Invalid number format" in error_output


def test_cli_insufficient_arguments() -> None:
    """Test CLI with insufficient arguments - should show error."""
    with patch('sys.argv', ['calculator', 'add', '5']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Usage" in error_output or "arguments" in error_output


def test_cli_too_many_arguments() -> None:
    """Test CLI with too many arguments - should show error."""
    with patch('sys.argv', ['calculator', 'add', '5', '3', '1']):
        from src.calculator.__main__ import main
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            with pytest.raises(SystemExit):
                main()
        error_output = captured_output.getvalue().strip()
        assert "Usage" in error_output or "arguments" in error_output


def test_cli_help_command() -> None:
    """Test CLI with help command - should show usage information."""
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