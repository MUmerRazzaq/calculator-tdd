from typing import Union
import pytest
from src.calculator import divide


def test_divide_positive_integers() -> None:
    """Test dividing positive integers - basic functionality."""
    assert divide(6, 3) == 2
    assert divide(10, 5) == 2
    assert divide(7, 1) == 7


def test_divide_by_one() -> None:
    """Test dividing by one - identity property."""
    assert divide(5, 1) == 5
    assert divide(-5, 1) == -5
    assert divide(0, 1) == 0


def test_divide_number_by_itself() -> None:
    """Test dividing a number by itself - should equal 1."""
    assert divide(5, 5) == 1
    assert divide(-5, -5) == 1
    assert divide(100, 100) == 1


def test_divide_negative_numbers() -> None:
    """Test dividing negative numbers - all sign combinations."""
    assert divide(-6, -3) == 2   # negative / negative = positive
    assert divide(-10, -5) == 2
    assert divide(6, -3) == -2   # positive / negative = negative
    assert divide(-6, 3) == -2   # negative / positive = negative


def test_divide_floats() -> None:
    """Test dividing floating point numbers with precision handling."""
    assert divide(5.0, 2.0) == pytest.approx(2.5)
    assert divide(7.5, 2.5) == pytest.approx(3.0)
    assert divide(-4.5, 1.5) == pytest.approx(-3.0)


def test_divide_large_numbers() -> None:
    """Test dividing very large numbers - no overflow issues."""
    assert divide(10**15, 10**5) == 10**10
    assert divide(1000000000000, 1000) == 1000000000


def test_divide_by_small_numbers() -> None:
    """Test dividing by small decimal numbers (resulting in large numbers)."""
    assert divide(10, 0.1) == pytest.approx(100.0)
    assert divide(5, 0.25) == pytest.approx(20.0)


def test_divide_small_by_large_numbers() -> None:
    """Test dividing small numbers by large numbers (resulting in small decimals)."""
    assert divide(1, 100) == pytest.approx(0.01)
    assert divide(0.5, 10) == pytest.approx(0.05)


def test_divide_integer_by_float() -> None:
    """Test dividing integers by floating point numbers."""
    assert divide(10, 2.5) == pytest.approx(4.0)
    assert divide(7, 1.75) == pytest.approx(4.0)


def test_divide_float_by_integer() -> None:
    """Test dividing floating point numbers by integers."""
    assert divide(7.5, 3) == pytest.approx(2.5)
    assert divide(-10.5, 5) == pytest.approx(-2.1)