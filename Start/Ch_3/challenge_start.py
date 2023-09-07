# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import pprint
import string

test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE
l = len(test_str)

nums = len([c for c in test_str if c.isnumeric()])

punct = len([c for c in test_str if c in string.punctuation])

unique = "".join({c for c in test_str if c.isalpha()})

# print the data
str_data = {
    "Length: ": l,
    "Digits: ": nums,
    "Punctuation: ": punct,
    "Unique Letters: ": unique,
    "Unique Count: ": len(unique),
}
pprint.pp(str_data)
