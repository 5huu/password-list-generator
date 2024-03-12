# password-list-generator

This tool generates passwords by combining a given set of words and seperators.

## Overview

The Password List Generator tool systematically creates passwords by exploring every possible combination of the provided words within the specified length range and separator.

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
python passwordgen.py -min <min_length> -max <max_length> -separator <separator> -w <word1> <word2> ...
```
&nbsp;&nbsp;&nbsp;The generated passwords will be saved to a file named `passwordlist.txt` in the same directory.
   
## Arguments

* -min <min_length>: Minimum length of passwords (default: 1).
* -max <max_length>: Maximum length of passwords (default: 4).
* -separator <separator>: Separator between words in passwords (default: '').
* -w, --words <words>: List of words for password generation.

## Example
The following command generate passwords with lengths ranging from 1 to 3, separated by underscores, and using the words "love," "banana," and "cat":
```
python passwordgen.py -min 1 -max 3 -separator '_' -w love banana cat
```
