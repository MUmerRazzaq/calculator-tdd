"""Calculator module with basic arithmetic operations."""


def add(a: float | int, b: float | int) -> float | int:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a: float | int, b: float | int) -> float | int:
    """
    Subtract the second number from the first number.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        The difference of a and b (a - b)
    """
    return a - b


def multiply(a: float | int, b: float | int) -> float | int:
    """
    Multiply two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        The product of a and b
    """
    return a * b


def divide(a: float | int, b: float | int) -> float:
    """
    Divide the first number by the second number.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        The quotient of a divided by b
    """
    return a / b