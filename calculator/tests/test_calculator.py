from typing import Union
import pytest
from src.calculator import multiply


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