def validate_positive_numbers(func):
    """Decorator to validate that the arguments are positive numbers."""
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("All arguments must be positive.")
        return func(*args, **kwargs)
    return wrapper