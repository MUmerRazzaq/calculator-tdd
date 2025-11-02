from typing import Union
import pytest
from src.calculator import add, subtract, multiply


def test_add_positive_integers() -> None:
    """Test adding two positive integers - basic functionality."""
    assert add(2, 3) == 5
    assert add(10, 5) == 15
    assert add(1, 1) == 2


def test_add_zero() -> None:
    """Test adding zero with other numbers - identity property."""
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, -5) == -5
    assert add(-5, 0) == -5


def test_add_negative_numbers() -> None:
    """Test adding negative numbers - all sign combinations."""
    assert add(-2, -3) == -5
    assert add(-10, -5) == -15
    assert add(-1, -1) == -2
    assert add(5, -3) == 2
    assert add(-5, 3) == -2
    assert add(10, -10) == 0


def test_add_floats() -> None:
    """Test adding floating point numbers with precision handling."""
    assert add(2.5, 3.7) == pytest.approx(6.2)
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(-1.5, 2.7) == pytest.approx(1.2)
    assert add(0.0001, 0.0002) == pytest.approx(0.0003)
    assert add(-0.0001, 0.0001) == pytest.approx(0)


def test_add_large_numbers() -> None:
    """Test adding very large numbers - no overflow issues."""
    assert add(10**10, 10**10) == 2 * (10**10)
    assert add(999999999999, 1) == 1000000000000


def test_add_integer_and_float() -> None:
    """Test adding integers with floating point numbers."""
    assert add(1, 2.5) == pytest.approx(3.5)
    assert add(5.5, 4) == pytest.approx(9.5)
    assert add(-3, 2.7) == pytest.approx(-0.3)


def test_subtract_positive_integers() -> None:
    """Test subtracting positive integers - basic functionality."""
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5
    assert subtract(1, 1) == 0


def test_subtract_zero() -> None:
    """Test subtracting zero - identity property."""
    assert subtract(5, 0) == 5
    assert subtract(0, 0) == 0
    assert subtract(-5, 0) == -5


def test_subtract_negative_results() -> None:
    """Test cases where subtraction results in negative numbers."""
    assert subtract(3, 5) == -2
    assert subtract(-5, 3) == -8
    assert subtract(0, 5) == -5


def test_subtract_negative_numbers() -> None:
    """Test subtracting negative numbers - all sign combinations."""
    assert subtract(-2, -3) == 1  # -2 - (-3) = -2 + 3 = 1
    assert subtract(-10, -5) == -5  # -10 - (-5) = -10 + 5 = -5
    assert subtract(5, -3) == 8  # 5 - (-3) = 5 + 3 = 8
    assert subtract(-5, 3) == -8  # -5 - 3 = -8


def test_subtract_floats() -> None:
    """Test subtracting floating point numbers with precision handling."""
    assert subtract(5.5, 2.2) == pytest.approx(3.3)
    assert subtract(0.3, 0.1) == pytest.approx(0.2)
    assert subtract(-1.7, 2.5) == pytest.approx(-4.2)
    assert subtract(0.0003, 0.0001) == pytest.approx(0.0002)


def test_subtract_large_numbers() -> None:
    """Test subtracting very large numbers - no overflow issues."""
    assert subtract(10**10, 10**9) == 9 * (10**9)
    assert subtract(1000000000000, 1) == 999999999999


def test_subtract_integer_and_float() -> None:
    """Test subtracting integers with floating point numbers."""
    assert subtract(5, 2.5) == pytest.approx(2.5)
    assert subtract(5.5, 2) == pytest.approx(3.5)


def test_multiply_positive_integers() -> None:
    """Test multiplying positive integers - basic functionality."""
    assert multiply(2, 3) == 6
    assert multiply(10, 5) == 50
    assert multiply(7, 8) == 56


def test_multiply_by_one() -> None:
    """Test multiplying by one - identity property."""
    assert multiply(5, 1) == 5
    assert multiply(1, 5) == 5
    assert multiply(1, 1) == 1
    assert multiply(-5, 1) == -5


def test_multiply_by_zero() -> None:
    """Test multiplying by zero - zero property."""
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0
    assert multiply(-5, 0) == 0
    assert multiply(0, -5) == 0


def test_multiply_negative_numbers() -> None:
    """Test multiplying negative numbers - all sign combinations."""
    assert multiply(-2, -3) == 6  # negative * negative = positive
    assert multiply(-10, -5) == 50
    assert multiply(5, -3) == -15  # positive * negative = negative
    assert multiply(-5, 3) == -15  # negative * positive = negative


def test_multiply_floats() -> None:
    """Test multiplying floating point numbers with precision handling."""
    assert multiply(2.5, 4.0) == pytest.approx(10.0)
    assert multiply(0.1, 0.2) == pytest.approx(0.02)
    assert multiply(-1.5, 2.0) == pytest.approx(-3.0)
    assert multiply(1.5, 2.5) == pytest.approx(3.75)


def test_multiply_large_numbers() -> None:
    """Test multiplying very large numbers - no overflow issues."""
    assert multiply(10**10, 10**5) == 10**15
    assert multiply(1000000, 1000000) == 1000000000000


def test_multiply_small_numbers() -> None:
    """Test multiplying very small numbers."""
    assert multiply(0.001, 0.001) == pytest.approx(0.000001)
    assert multiply(0.1, 0.1) == pytest.approx(0.01)


def test_multiply_integer_and_float() -> None:
    """Test multiplying integers with floating point numbers."""
    assert multiply(5, 2.5) == pytest.approx(12.5)
    assert multiply(3.5, 4) == pytest.approx(14.0)
    assert multiply(-3, 2.5) == pytest.approx(-7.5)


def test_multiply_associative_property() -> None:
    """Test associative property: a * (b * c) == (a * b) * c."""
    assert multiply(2, multiply(3, 4)) == multiply(multiply(2, 3), 4)
    assert multiply(1.5, multiply(2, 3)) == pytest.approx(multiply(multiply(1.5, 2), 3))


def test_multiply_commutative_property() -> None:
    """Test commutative property: a * b == b * a."""
    assert multiply(5, 3) == multiply(3, 5)
    assert multiply(2.5, 4) == pytest.approx(multiply(4, 2.5))
    assert multiply(-3, 7) == multiply(7, -3)