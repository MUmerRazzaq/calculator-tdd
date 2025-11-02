from typing import Union
import pytest
from src.calculator import add


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