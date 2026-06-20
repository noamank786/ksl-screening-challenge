def get_input_list():
    """Accept a list of integers as input."""
    raw_input_str = input("Enter integers separated by spaces: ")
    numbers = [int(x) for x in raw_input_str.split()]
    return numbers