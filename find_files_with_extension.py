# Write a script to find all files with a specific extension in a directory.
# The script should take the directory path and the extension as input.
# The script should print the list of files with the specified extension.
# Example: find_files_with_extension.py /path/to/directory py
# Output: ['file1.py', 'file2.py', 'file3.py']
# You can use the argparse module to parse the command-line arguments.
# Directory path and extension are mandatory arguments.
# It should check sub directories as well.

import argparse
import os


def find_files_with_extension(directory, extension):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        # print(f'dirpath: {dirpath}, dirnames: {dirnames}, filenames: {filenames}')
        for file in filenames:
            if file.endswith(extension):
                files.append(os.path.join(dirpath, file))
    return files


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('directory', type=str, help='Directory path')
    argparse.add_argument('extension', type=str, help='File extension')
    args = argparse.parse_args()
    print(find_files_with_extension(args.directory, args.extension))
