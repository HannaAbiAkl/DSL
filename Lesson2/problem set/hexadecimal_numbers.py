import ply.lex as lex

tokens = ('NUM', 'ID')

def t_NUM_hex(token):
    
    r"0x[0-9a-f]+"
    
    token.value = token.value[2:]
    
    result = 0
    
    for i in range(len(token.value)-1, -1, -1):
        
        if ord(token.value[i]) >= 97:
            
            tem = ord(token.value[i])-97+10
            
            result = result + tem*(16**(len(token.value)-i-1))
        
        else:

            result = result + int(token.value[i])*(16**(len(token.value)-i-1))
    
    token.value = result
    
    token.type = "NUM"
    
    return token

def t_ID(token):
    
    r"[a-zA-Z]+"
    
    token.value = token.value
    token.type = "ID"
    
    return token
    
def t_NUM_decimal(token):
    
  r'[0-9]+'
  
  token.value = int(token.value) # won't work on hex numbers!
  token.type = 'NUM'
  
  return token

t_ignore = ' \t\v\r'

def t_error(t):
    
  print ("Lexer: unexpected character " + t.value[0])
  
  t.lexer.skip(1) 

lexer = lex.lex() 

def test_lexer(input_string):
    
  lexer.input(input_string)
  
  result = [ ] 
  
  while True:
      
    tok = lexer.token()
    
    if not tok: break

    result = result + [(tok.type, tok.value)]
    
  return result

question1 = "0x19 equals 25"
answer1 = [('NUM', 25), ('ID', 'equals'), ('NUM', 25) ]

print((test_lexer(question1) == answer1))

question2 = "0xfeed MY 0xface" 
answer2 = [('NUM', 65261), ('ID', 'MY'), ('NUM', 64206) ]

print(test_lexer(question2) == answer2)

question3 = "tricky 0x0x0x"   # attention, there are only 4 pairs of 0 & x in ans
answer3 = [('ID', 'tricky'), ('NUM', 0), ('ID', 'x'), ('NUM', 0), ('ID', 'x')]

print(test_lexer(question3) == answer3)

question4 = "in 0xdeed"
print(test_lexer(question4))

question5 = "where is the 0xbeef"
print(test_lexer(question5))