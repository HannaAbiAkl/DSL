# Learning Regular Expressions

# Define a variable regexp that matches the left 3 strings but not the right 3.

#   Yes     No
#   aaa    aabbb
#   abb    aaccc
#   acc     bc


regexp = r"(a+?(a+|(b|c){2}))"

import re 

tests = [("aaa", True), ("abb", True), ("acc", True), ("aabbb", False), ("aaccc", False), ("bc", False)]

for r, ans in tests:
    print((re.findall(regexp, r)[0][0]) == r if re.findall(regexp, r) else False)
