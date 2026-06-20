def get_input_list():
    raw_input_str = input("Enter integers separated by spaces: ")
    numbers = [int(x) for x in raw_input_str.split()]
    return numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]

def sort_descending(numbers):
    return sorted(numbers, reverse=True)

def display_results(original_list, sorted_primes):
    print("Sorted prime numbers (descending):", sorted_primes)
    print("Total elements processed:", len(original_list))


def main():
    numbers = get_input_list()
    primes = filter_primes(numbers)
    sorted_primes = sort_descending(primes)
    display_results(numbers, sorted_primes)


if __name__ == "__main__":
    main()
