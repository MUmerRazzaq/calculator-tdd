"""Calculator CLI module for performing arithmetic operations from command line."""

import sys
from typing import Union
from . import add, subtract, multiply, divide


def parse_arguments() -> tuple[str, float, float]:
    """
    Parse command line arguments.
    
    Returns:
        A tuple containing (operation, num1, num2)
        
    Raises:
        SystemExit: If arguments are invalid
    """
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        show_help()
        sys.exit(0)
    
    if len(sys.argv) != 4:
        print("Usage: python -m calculator <operation> <num1> <num2>", file=sys.stderr)
        print("Example: python -m calculator add 5 3", file=sys.stderr)
        sys.exit(1)
    
    operation = sys.argv[1].lower()
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Invalid number format", file=sys.stderr)
        sys.exit(1)
    
    return operation, num1, num2


def show_help() -> None:
    """Display help information for the calculator CLI."""
    help_text = """
Calculator CLI - Perform arithmetic operations from command line

Usage: python -m calculator <operation> <num1> <num2>

Operations:
  add       - Addition (num1 + num2)
  subtract  - Subtraction (num1 - num2)
  multiply  - Multiplication (num1 * num2)
  divide    - Division (num1 / num2)

Examples:
  python -m calculator add 5 3
  python -m calculator multiply 4.5 2
  python -m calculator divide 10 3
"""
    print(help_text)


def perform_operation(operation: str, num1: float, num2: float) -> Union[float, int]:
    """
    Perform the specified operation on the two numbers.
    
    Args:
        operation: The arithmetic operation to perform
        num1: First number
        num2: Second number
        
    Returns:
        The result of the operation
        
    Raises:
        SystemExit: If operation is not supported
    """
    if operation == 'add':
        return add(num1, num2)
    elif operation == 'subtract':
        return subtract(num1, num2)
    elif operation == 'multiply':
        return multiply(num1, num2)
    elif operation == 'divide':
        if num2 == 0:
            print("Error: Cannot divide by zero", file=sys.stderr)
            sys.exit(1)
        return divide(num1, num2)
    else:
        print(f"Error: Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Main function to run the calculator CLI."""
    try:
        operation, num1, num2 = parse_arguments()
        result = perform_operation(operation, num1, num2)
        print(result)
    except SystemExit:
        # Re-raise SystemExit to properly exit the program
        raise
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()