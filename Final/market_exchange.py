# Market Exchange
#
# Focus: Units 5 and 6, Interpreting and Environments
#
#
# In this problem you will use your knowledge of interpretation and
# environments to simulate a simple market. Here the "program" is not a
# list of JavaScript commands that describe webpage computation, but
# instead a list of economic commands that describe business transactions.  
#
# Our parse tree (or abstract syntax tree) is a list of elements. Elements
# have three forms: has, buy and sell. "has" elements indicate that the
# given person begins with the given amount of money:
#
#       [ "klaus teuber", "has", 100 ] 
#
# "buy" elements indicate that the given person wants to purchase some
# item for the listed amount of money. For example:
#
#       [ "klaus teuber", "buy", "sheep", 50 ] 
#
# ... means that "klaus teuber" is interesting in buying the item
# "sheep" for 50 monetary units. For this assignment, that transaction will
# only happen if there is a seller also selling "sheep" for 50 (and if
# klaus actually has 50 or more monetary units). That is, both the item and
# the price must match exactly. The final type of element is "sell": 
#
#       [ "andreas seyfarth", "sell", "sheep" , 50 ] 
#
# This indicates that "andreas seyfarth" is willing to sell the item
# "sheep" for 50 monetary units. (Again, that transaction will only take
# place if there is a buyer wishing to purchase that item for exactly the
# same amount of money -- and if the buyer actually has at least that much
# money!) 
#
# All of the "has" commands will come first in the program.
#
# "buy" and "sell" elements only operate once per time they are listed. In
# this example: 
# 
#       [ "klaus teuber", "has", 100 ] 
#       [ "andreas seyfarth", "has", 50 ] 
#       [ "klaus teuber", "buy", "sheep", 50 ] 
#       [ "andreas seyfarth", "sell", "sheep" , 50 ] 
#
# klaus will buy "sheep" from andreas once, at which poin klaus will have
# 50 money and andreas will have 100. However, in this example:
#
#       [ "klaus teuber", "has", 100 ] 
#       [ "andreas seyfarth", "has", 50 ] 
#       [ "klaus teuber", "buy", "sheep", 50 ] 
#       [ "klaus teuber", "buy", "sheep", 50 ]          # listed twice
#       [ "andreas seyfarth", "sell", "sheep" , 50 ] 
#       [ "andreas seyfarth", "sell", "sheep" , 50 ]    # listed twice
# 
# klaus will buy "sheep" from andreas and then buy "sheep" from andreas
# again, at which point klaus will have 0 money and andreas will have 150. 
#
# Write a procedure evaluate() that takes a list of elements as an input.
# It should perform all possible transactions, in any order, until no more
# transactions are possible (e.g., because all "buy" and "sell" elements
# have been used and/or potential buyers do not have enough money left for
# their desired "buy"s). Your procedure should return an environment
# (a Python dictionary) mapping names to final money amounts (after all
# transactions have happened).  
#
# Hint: To avoid processing a "buy" or "sell" twice, you might either call
# yourself recursively with a smaller AST (i.e., with those two elements
# removed) or you can use Python's list.remove() to remove elements "in
# place". Example: 
#
# lst = [("a",1) , ("b",2) ]
# print lst
# [('a', 1), ('b', 2)]
# 
# lst.remove( ("a",1) )
# print lst
# [('b', 2)]

def evaluate(ast):
        # fill in your code here ...
    env = {}
    finished = False
    while not finished:
        finished = True
        for elt in ast:
            who = elt[0]
            elttype = elt[1]
            if elttype == "has":
                env[who] = elt[2]
                finished = False
                elt[1] = "skip"
            elif elttype == "buy":
                what = elt[2]
                howmuch = elt[3]
                for i in range(len(ast)):
                    if ast[i][1] == "sell"  and \
                       ast[i][2] == what    and \
                       env[who]  >= howmuch and \
                       ast[i][3] == howmuch:
                         elt[1] = "skip"
                         ast[i][1] = "skip"
                         env[who] -= howmuch
                         env[ast[i][0]] += howmuch
                         finished = False
    return env


# In test1, exactly one sell happens. Even though klaus still has 25 money
# left over, a "buy"/"sell" only happens once per time it is listed. 
test1 = [ ["klaus","has",50] ,
          ["wrede","has",80] ,
          ["klaus","buy","sheep", 25] ,
          ["wrede","sell","sheep", 25] , ] 

print(evaluate(test1) == {'klaus': 25, 'wrede': 105})

# In test2, klaus does not have enough money, so no transactions take place.
test2 = [ ["klaus","has",5] ,
          ["wrede","has",80] ,
          ["klaus","buy","sheep", 25] ,
          ["wrede","sell","sheep", 25] , ] 

print(evaluate(test2) == {'klaus': 5, 'wrede': 80})

# Wishful thinking, klaus! Although you want to buy sheep for 5 money and
# you even have 5 money, no one is selling sheep for 5 money. So no
# transactions happen.
test2b = [ ["klaus","has",5] ,
           ["wrede","has",80] ,
           ["klaus","buy","sheep", 5] ,
           ["wrede","sell","sheep", 25] , ] 

print(evaluate(test2b) == {'klaus': 5, 'wrede': 80})

# In test3, wrede does not have the 75 required to buy the wheat from
# andreas until after wrede sells the sheep to klaus. 
test3 = [ ["klaus","has",50] ,
          ["wrede","has",50] ,
          ["andreas","has",50] ,
          ["wrede","buy","wheat", 75] ,
          ["andreas","sell","wheat", 75] , 
          ["klaus","buy","sheep", 25] ,
          ["wrede","sell","sheep", 25] , 
          ] 
print(evaluate(test3 ) == {'andreas': 125, 'klaus': 25, 'wrede': 0})
