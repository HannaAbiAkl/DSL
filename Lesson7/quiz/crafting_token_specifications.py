# Crafting Token Specifications

# Define a variable regexp that matches numbers with 1 or more leading digits
# and an optional . followed by 0 or more digits.

regexp = r"[0-9]+?.[0-9]*"

import re

tests = [("123", True), ("1.2", True), ("1.", True), (".5", False), (".5.6", False), ("1..2", False)]

for r, ans in tests:
    print((re.findall(regexp, r) == [r]) == ans)
