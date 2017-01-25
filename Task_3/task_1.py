def func13(x):
	result = ''
	str=input("Введите, пожалуйста, строку: ")
	n=int(input("А теперь введите число повторов: "))
	for i in range(0, n):
		result += str + '\n'
	return result

def func46(x):
	m=int(input("Введите, пожалуйста, степень: "))
	return "%s в степени %s равно %s"%(x, m, x**m)

def func79(x):
	result = ""
	for i in range(0, 10):
		x+=1
		result+="%s \n" % x
	return result