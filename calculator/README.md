# Calculator-TDD

A comprehensive calculator application developed using Test-Driven Development (TDD) methodology. This project demonstrates the implementation of basic arithmetic operations (addition, subtraction, multiplication, division) with a command-line interface, comprehensive error handling, and thorough test coverage.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Command-Line Interface (CLI)**: Perform calculations directly from the command line
- **Comprehensive Error Handling**: Type validation, division by zero protection, overflow prevention
- **Full Test Coverage**: 63 tests covering all functionality and edge cases
- **Python 3.12+ Compatible**: Uses modern Python type hints with union syntax (`|`)

## TDD Approach

This project was built using Test-Driven Development methodology following the "Red-Green-Refactor" cycle:

1. **Red Phase**: Write a test for a new feature that initially fails
2. **Green Phase**: Write the minimum code needed to make the test pass
3. **Refactor Phase**: Improve the code while keeping all tests passing

The development process followed these stages:

### Feature Development Sequence
1. **Addition functionality** with comprehensive tests
2. **Subtraction functionality** with tests for all sign combinations
3. **Multiplication functionality** with tests including mathematical properties
4. **Division functionality** with special handling for division by zero
5. **CLI interface** with command-line argument parsing and user interaction
6. **Comprehensive error handling** including type validation and overflow protection

### Key TDD Principles Applied
- **"Make it work, make it right, make it fast"**: Started with basic functionality, then added robustness and error handling
- **Type Safety**: Used Python 3.12+ union syntax (`float | int`) for precise type hints
- **Edge Case Coverage**: Tests for zero values, negative numbers, floating point precision, large numbers
- **Error Handling**: Proper exceptions for invalid operations, type errors, and mathematical errors

## Project Structure

```
calculator/
├── src/
│   └── calculator/
│       ├── __init__.py      # Contains all arithmetic functions
│       └── __main__.py      # CLI module
├── tests/
│   ├── test_calculator.py   # Tests for arithmetic functions
│   ├── test_cli.py          # Tests for CLI interface
│   └── test_error_handling.py # Tests for error scenarios
└── pyproject.toml           # Project configuration
```

## Installation and Usage

### Prerequisites
- Python 3.12 or higher
- UV package manager

### Setup
```bash
git clone git@github.com:MUmerRazzaq/calculator-tdd.git
cd calculator-tdd
uv sync  # or use python -m venv and pip install
```

### CLI Usage
```bash
# Addition
python -m src.calculator add 5 3
# Output: 8.0

# Subtraction
python -m src.calculator subtract 10 4
# Output: 6.0

# Multiplication
python -m src.calculator multiply 6 7
# Output: 42.0

# Division
python -m src.calculator divide 15 3
# Output: 5.0

# View help
python -m src.calculator --help
```

### Direct API Usage
```python
from src.calculator import add, subtract, multiply, divide

result = add(10, 5)      # 15
result = subtract(10, 5) # 5
result = multiply(10, 5) # 50
result = divide(10, 5)   # 2.0
```

## Testing

The project includes comprehensive tests covering:

- **Arithmetic Operations**: All basic operations with various number types
- **Edge Cases**: Zero values, negative numbers, large numbers, floating point precision
- **Error Handling**: Division by zero, invalid inputs, type validation, overflow conditions
- **CLI Interface**: All command-line scenarios, error messages, help text
- **Mathematical Properties**: Associative, commutative properties for multiplication

Run tests with:
```bash
python -m pytest tests/ -v
```

## Error Handling

The calculator includes robust error handling:

- **Division by Zero**: Raises `ZeroDivisionError` with descriptive message
- **Type Validation**: Checks for proper numeric inputs
- **Overflow Protection**: Prevents operations resulting in extremely large numbers
- **CLI Error Messages**: Clear error messages for invalid operations and formats

## Development Methodology

This project demonstrates the benefits of TDD:

- **Higher Quality Code**: All functionality is covered by tests
- **Better Design**: Features developed incrementally with clear interfaces
- **Refactoring Confidence**: Tests ensure changes don't break existing functionality
- **Documentation**: Tests serve as executable specifications

## License

This project is open source and available under the MIT License.