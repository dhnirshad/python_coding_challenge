# Implement a function to reverse a string without using any built-in reverse functions.
# Example: reverse_string('hello') -> 'olleh'
import argparse


def reverse_string(s):
    return s[::-1]


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('string', type=str, help='String to reverse')
    print(reverse_string(argparse.parse_args().string))
