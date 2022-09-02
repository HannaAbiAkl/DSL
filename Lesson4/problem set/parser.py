def addtochart(theset,index,elt):
  if not (elt in theset[index]):
    theset[index] = [elt] + theset[index]
    return True
  return False

def closure (grammar, i, x, ab, cd, j):
  next_states = [(rule[0], [], rule[1], i) for rule in grammar if cd != [] and rule[0] == cd[0]]
  return next_states

def shift (tokens, i, x, ab, cd, j):
    if cd != [] and tokens[i] == cd[0]:
      return (x, ab + [cd[0]], cd[1:], j)
    else:
      return None

def reductions(chart, i, x, ab, cd, j):
    return [
      (jstate[0], jstate[1] + [x], (jstate[2])[1:], jstate[3]) \
      for jstate in chart[j] \
      if cd == [] and jstate[2] != [] and (jstate[2])[0] == x
    ]

def parse(tokens,grammar):
  tokens = tokens + [ "end_of_input_marker" ]
  chart = {}
  start_rule = grammar[0] # for example, S -> P
  for i in range(len(tokens)+1):
    chart[i] = [ ]
  start_state = (start_rule[0], [], start_rule[1], 0)
  chart[0] = [ start_state ]
  for i in range(len(tokens)):
    while True:
      changes = False
      for state in chart[i]:
        # State ===   x -> a b . c d , j
        x = state[0]
        ab = state[1]
        cd = state[2]
        j = state[3]

        # Current State ==   x -> a b . c d , j
        # Option 1: For each grammar rule c -> p q r
        # (where the c's match)
        # make a next state               c -> . p q r , i
        # English: We're about to start parsing a "c", but
        #  "c" may be something like "exp" with its own
        #  production rules. We'll bring those production rules in.
        next_states = closure(grammar, i, x, ab, cd, j)
        for next_state in next_states:
          changes = addtochart(chart,i,next_state) or changes

        # Current State ==   x -> a b . c d , j
        # Option 2: If tokens[i] == c,
        # make a next state               x -> a b c . d , j
        # in chart[i+1]
        # English: We're looking for to parse token c next
        #  and the current token is exactly c! Aren't we lucky!
        #  So we can parse over it and move to j+1.
        next_state = shift(tokens, i, x, ab, cd, j)
        if next_state != None:
          any_changes = addtochart(chart, i+1, next_state) or any_changes

        # Current State ==   x -> a b . c d , j
        # Option 3: If cd is [], the state is just x -> a b . , j
        # for each p -> q . x r , l in chart[j]
        # make a new state                p -> q x . r , l
        # in chart[i]
        # English: We just finished parsing an "x" with this token,
        #  but that may have been a sub-step (like matching "exp -> 2"
        #  in "2+3"). We should update the higher-level rules as well.
        next_states = reductions(chart, i, x, ab, cd, j)
        for next_state in next_states:
          changes = addtochart(chart,i,next_state) or changes

      # We're done if nothing changed!
      if not changes:
        break

## Comment this block back in if you'd like to see the chart printed.
  for i in range(len(tokens)): # print out the chart
   print("== chart " + str(i))
   for state in chart[i]:
     x = state[0]
     ab = state[1]
     cd = state[2]
     j = state[3]
     print("    " + x + " ->"),
     for sym in ab:
       print(" " + sym),
     print(" ."),
     for sym in cd:
       print(" " + sym),
     print("  from " + str(j))

  accepting_state = (start_rule[0], start_rule[1], [], 0)
  return accepting_state in chart[len(tokens)-1]


grammar = [
  ("S", ["P" ]) ,           # S -> P
  ("P", ["(" , "P", ")" ]), # P -> (P)
  ("P", [ ]) ,              # P ->
]
tokens = [ "(", "(", ")", ")"]


result=parse(tokens, grammar)
print(result)