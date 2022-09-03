def interpret(trees):
	global_env = (None, {"javascript output" : ""})
	for elt in trees:
		eval_elt(elt, global_env)
	return (global_env[1])["javascript output"]