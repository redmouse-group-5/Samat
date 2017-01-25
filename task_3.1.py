def str_split(mystr):
	result=""
	for word in mystr.split():
		result+="%s - %s"%(word, len(word))
	return result

print (str_split(input("Введите строку: ")))

def mypow(*arg):
	mypow=1
	result = list()
	for i in arg:
		result.append(i**mypow)
		mypow=i
	return result

print (mypow(2, 3, 2, 3, 4))
