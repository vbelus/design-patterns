# Decorator Examples for Mathematical Functions

This directory demonstrates the use of Python's `@` decorator syntax through various examples applied to mathematical functions. Decorators in Python allow you to modify or extend the behavior of functions or methods without changing their code directly. The examples here are implemented using Python classes and custom decorators.

---

## **Directory Structure**

- **`cache_decorator.py`**:  
  Implements a custom caching mechanism to optimize functions by storing their results. This helps avoid redundant computations for the same inputs.

- **`logging_decorator.py`**:  
  Logs the inputs and outputs of decorated functions, making it easy to track their behavior during execution.

- **`validate_positive_decorator.py`**:  
  Ensures that all numerical inputs to decorated functions are positive. Raises a `ValueError` for invalid inputs.

- **`example.py`**:  
  Combines all the decorators to demonstrate their usage with a Fibonacci function. The example uses Python's `@` syntax to stack the decorators elegantly.