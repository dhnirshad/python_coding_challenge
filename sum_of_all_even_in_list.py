# Given a list of integers, write a function to return the sum of all even numbers in the list.
# Example of function: sum_of_all_even([1, 2, 3, 4, 5, 6]), Returns-> 12
# You can use the argparse module to parse the command-line arguments.
# List of integers is a mandatory argument like [1, 2, 3, 4, 5, 6]
# Example sum_of_all_even_in_list.py "[1, 2, 3, 4, 5, 6]", Output: 12

import argparse
import ast


def sum_of_all_even(list_of_integers):
    return sum([i for i in list_of_integers if i % 2 == 0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', type=str, help='Comma separated list of integers')
    args = parser.parse_args()
    numbers = ast.literal_eval(args.numbers)
    print(sum_of_all_even(numbers))
