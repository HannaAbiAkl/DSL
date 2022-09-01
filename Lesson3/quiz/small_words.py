# Small Words

# Write a Python generator function called small_words 
# that accepts a list of strings as input and yields 
# those that are at most 3 letters long.

def small_words(strlist):
    for x in strlist:
        if len(x) <= 3:
            yield x
