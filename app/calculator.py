class Calculator:
    """A simple calculator app to demonstrate Factory.ai test automation."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def sqrt(self, n):
        if n < 0:
            raise ValueError("Cannot take sqrt of a negative number")
        return n ** 0.5

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def percentage(self, value, total):
        if total == 0:
            raise ValueError("Total cannot be zero")
        return (value / total) * 100