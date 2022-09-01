# Expanding Exp
# This is very, very difficult.
# Here's a hint. You're going to need yield with high probability, 
# and you may also want to end up using list comprehensions.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]


def expand(tokens, grammar):
    for pos in range(len(tokens)):
        for rule in grammar:
            if tokens[pos] == rule[0]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]   
                
            
depth = 1
utterances = [["exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    print(sentence)
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']