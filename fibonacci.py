def fibonacci_sequence(n):
    """
    Returns a list containing the first n Fibonacci numbers.
    
    Args:
        n (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: The first n numbers in the Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the sequence with the first two numbers
    fib_sequence = [0, 1]
    
    # Generate subsequent numbers
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Example usage
if __name__ == "__main__":
    # Test with different values of n
    test_values = [0, 1, 5, 10]
    for n in test_values:
        result = fibonacci_sequence(n)
        print(f"First {n} Fibonacci numbers: {result}")