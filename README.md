# password-list-generator

This tool generates passwords by combining a given set of words and/or numbers.

## Overview

The Password List Generator tool systematically creates passwords by exploring every possible combination of the provided words and/or numbers within the specified length range and separator.

## Usage

1. Clone the repository:
```
git clone https://github.com/5huu/password-list-generator.git
```
2. Navigate to the repository directory:
```
cd password-list-generator
```
3. Run the script with the desired parameters:
```
python passwordgen.py -min <min_length> -max <max_length> -separator <separator> -w <word1> <word2> ... -n <number1> <number2> ...
```
&nbsp;&nbsp;&nbsp;The generated passwords will be saved to a file named `passlist.txt` in the same directory.
   
## Arguments

* -min <min_length>: Minimum length of passwords (default: 1).
* -max <max_length>: Maximum length of passwords (default: 4).
* -separator <separator>: Separator between words in passwords (default: '').
* -w, --words <words>: List of words for password generation.
* -n, --numbers <numbers>: List of numbers for password generation.

## Example
The command generates passwords with lengths ranging from 2 to 3, separated by hyphens, using the words "banana" and "cat" and the numbers 10 and 20:
```
python passwordgen.py -min 2 -max 3 -separator '-' -w banana cat -n 10 20
```
