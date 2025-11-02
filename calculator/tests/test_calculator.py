from typing import Union
import pytest
from src.calculator import add, subtract


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