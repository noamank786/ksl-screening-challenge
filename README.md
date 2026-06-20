# KSL Screening Challenge

A command-line utility that filters prime numbers from a list of integers and sorts them in descending order. Built as part of the Kaviv Software Labs technical screening challenge.

## What It Does

1. Accepts a list of integers as input
2. Filters out all prime numbers from the list
3. Sorts the remaining prime numbers in descending order
4. Prints the sorted list along with a count of total elements processed

## Project Structure

```
ksl-screening-challenge/
├── main.py
└── README.md
```

The logic is organized into separate, reusable functions:

- `get_input_list()` — reads integers from user input
- `is_prime(n)` — checks whether a single number is prime
- `filter_primes(numbers)` — extracts primes from the list
- `sort_descending(numbers)` — sorts numbers in descending order
- `display_results(original_list, sorted_primes)` — prints results and element count
- `main()` — runs the full program

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/ksl-screening-challenge.git
   cd ksl-screening-challenge
   ```

2. Run the script:
   ```
   python main.py
   ```

3. When prompted, enter a list of integers separated by spaces:
   ```
   Enter integers separated by spaces: 2 3 4 5 10 11 15 17
   ```

4. The program will output the sorted prime numbers and the total count of elements processed:
   ```
   Sorted prime numbers (descending): [17, 11, 5, 3, 2]
   Total elements processed: 8
   ```

## Example

**Input:**
```
4 7 9 13 18 23 25 29
```

**Output:**
```
Sorted prime numbers (descending): [29, 23, 13, 7]
Total elements processed: 8
```
