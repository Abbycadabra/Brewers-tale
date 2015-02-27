# GameUti

def is_list(obj):
	return str(type(obj)) == "<type 'list'>"

def is_dict(obj):
	return str(type(obj)) == "<type 'dict'>"

def is_str(obj):
	return str(type(obj)) == "<type 'str'>" 

def recurse_list(obj):
	result = ""
	for value in obj:
		if is_list(value):
			recurse_list(value)
		elif is_dict(value):
			recurse_dict(value)
		else:
			result += key + ": " + value + "\n"
	return result

def recurse_dict(obj):
	print is_list([])
	print is_dict({})
	print is_str("")
	result = ""
	for key, value in obj.iteritems():
		if is_list(value):
			recurse_list(value)
		elif is_dict(value):
			recurse_dict(value)
		else:
			result += key + ": " + value + "\n"
	return result