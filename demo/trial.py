"""Sample code for illustrating python package setup and test-driven development."""

# First code written for python package test.
def square(x):
    """Finds the square of the input.
    
    Args:
        x (float): The number to be squared.

    Returns:
        x2 (float): The squared number.
    """

    return x**2

# Second code written for test-driven development workflow.
def factorial(n):
    """Factorial calculates the factorial of the provided integer.

    Args:
        n (int): The value that the factorial will be computed from. 

    Returns:
        fact (int): The factorial of n. 

    Raises:
        ValueError: If n is not an integer.
    """

    if not isinstance(n,int):
        raise ValueError("The input to factorial must be an integer.")

    if n < 0:
        fact = 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact = i*fact

    return fact
