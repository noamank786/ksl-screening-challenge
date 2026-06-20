def get_input_list():
    """Accept a list of integers as input."""
    raw_input_str = input("Enter integers separated by spaces: ")
    numbers = [int(x) for x in raw_input_str.split()]
    return numbers
    
    def is_prime(n):
    """Check if a single number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_primes(numbers):
    """Return only the prime numbers from the list."""
    return [num for num in numbers if is_prime(num)]