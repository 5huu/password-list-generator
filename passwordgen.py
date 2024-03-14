import argparse
from itertools import permutations

def generate_passwords(words, numbers, min_length=1, max_length=None, separator=''):
    passwords = []
    if max_length is None:
        max_length = len(words) + len(numbers)

    for r in range(min_length, max_length + 1):
        for perm in permutations(words + numbers, r):
            password = separator.join(map(str, perm))
            passwords.append(password)

    return passwords

def write_to_file(passwords, filename='passlist.txt'):
    with open(filename, 'w') as f:
        f.write('\n'.join(passwords))
    print(f"Word list generated and saved to {filename}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-min', type=int, default=1, help='Minimum length of passwords')
    parser.add_argument('-max', type=int, default=4, help='Maximum length of passwords')
    parser.add_argument('-separator', type=str, default='', help='Separator between words in passwords')
    parser.add_argument('-w', '--words', nargs='+', help='List of words for password generation')
    parser.add_argument('-n', '--numbers', nargs='+', type=int, help='List of numbers for password generation')
    args = parser.parse_args()

    min_length = args.min
    max_length = args.max
    separator = args.separator
    words = args.words or []
    numbers = args.numbers or []

    passwords = generate_passwords(words, numbers, min_length, max_length, separator)
    write_to_file(passwords)

