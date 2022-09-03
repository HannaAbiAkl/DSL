# Environment Needs

def env_lookup(vname, env):
	# env = (parent, dictionary)
	if vname in env[1]:	# do we have it?
		return (env[1])[vname]  
	elif env[0] == None: # are we the global enviroment?
		return None
	else: # if not global, ask parents
		return env_lookup(vname, env[0]) 



def env_update(vname, value, env):
	if vname in env[1]:
		(env[1])[vname] = value
	elif not (env[0] == None):
		env_update(vname, value, env[0])