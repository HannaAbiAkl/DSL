# QUIZ -- HTML Interpreter on JavaScript elements
def interpret(trees):
	for tree in trees:
		treetype = tree[0]
		if treetype == "word-element":
			graphics.word(node[1])
		elif treetype == "javascript-element":
			jstext = tree[1] # "document.write(55);"
			jslexer = lex.lex(module=jstokens)
			jsparser = yacc.yacc(module=jsgrammar)
			jstree = jsparser.parse(jstext, lexer=jslexer)
			# jstree is a parse tree for JavaScript
			result = jsinterp.interpret(jstree)
			graphics.word(result)