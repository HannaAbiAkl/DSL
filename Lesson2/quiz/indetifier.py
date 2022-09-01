# Identifier

# Identifiers are textual string descriptions that refer to program elements,
# such as variables and functions. Write a indentifier token rule for Javascript identifiers.

# The token rule should match:

#   factorial
#   underscore_separated
#   mystery
#   ABC

# The token rule should not match:

#   _starts_wrong
#   123


def t_IDENTIFIER(token):
    r'(?:[a-z]+_*[A-Z]*)+|(?:[A-Z]+_*[a-z]*)+'
    return token