# Recall: Writing A Lexer: Token Definitions
def t_javascript(token):
	r'\<script\ type=\"text\/javascript\"\>'
	token.lexer.code_start = token.lexer.lexpos
	token.lexer.begin("javascript")

def t_javascript_end(token):
	r'\<\/script\>' #</script>
	token.value = token.lexer.lexdata[token.lexer.code_start: token.lexer.lexpos-9]
	token.type = 'JAVASCRIPT'
	token.lexer.lineno += token.value.count('\n')
	token.lexer.begin('INITIAL')
	return token