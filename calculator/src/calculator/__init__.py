"""Calculator module with basic arithmetic operations and enhanced error handling."""

import math


def _validate_number(value: object) -> None:
    """
    Validate that the value is a number (int or float).
    
    Args:
        value: The value to validate
        
    Raises:
        TypeError: If value is not int or float
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected int or float, got {type(value).__name__}")


def _check_result_range(result: float | int) -> None:
    """
    Check if the result is within acceptable range.
    Raises OverflowError for results that are too large.
    
    Args:
        result: The result to check
        
    Raises:
        OverflowError: If result is too large
    """
    # Define a reasonable maximum value to prevent extremely large results
    MAX_VALUE = 10**100
    
    # For floats, check if it's infinity or exceeds max value
    if isinstance(result, float):
        if math.isinf(result) or abs(result) > MAX_VALUE:
            raise OverflowError(f"Result {result} is too large (max: {MAX_VALUE})")
    
    # For integers, check if absolute value exceeds max value
    elif isinstance(result, int):
        if abs(result) > MAX_VALUE:
            raise OverflowError(f"Result {result} is too large (max: {MAX_VALUE})")


def add(a: float | int, b: float | int) -> float | int:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If either argument is not a number
        OverflowError: If the result is too large
    """
    _validate_number(a)
    _validate_number(b)
    result = a + b
    _check_result_range(result)
    return result


def subtract(a: float | int, b: float | int) -> float | int:
    """
    Subtract the second number from the first number.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        The difference of a and b (a - b)
        
    Raises:
        TypeError: If either argument is not a number
        OverflowError: If the result is too large
    """
    _validate_number(a)
    _validate_number(b)
    result = a - b
    _check_result_range(result)
    return result


def multiply(a: float | int, b: float | int) -> float | int:
    """
    Multiply two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        The product of a and b
        
    Raises:
        TypeError: If either argument is not a number
        OverflowError: If the result is too large
    """
    _validate_number(a)
    _validate_number(b)
    result = a * b
    _check_result_range(result)
    return result


def divide(a: float | int, b: float | int) -> float:
    """
    Divide the first number by the second number.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        TypeError: If either argument is not a number
        ZeroDivisionError: If b is zero
        OverflowError: If the result is too large
    """
    _validate_number(a)
    _validate_number(b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    result = a / b
    _check_result_range(result)
    return result