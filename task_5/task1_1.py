class task1_1():
	
	def __init__(self, x):
		self.x = x
		if 0<=self.x<=3:	
			print (self.func13())
		elif 4<=self.x<=6:
			print (self.func46())
		elif 7<=self.x<=9:
			print (self.func79())
		else:
		    print ("Error")
	
	def func13(self):
		result = ''
		str=(input("Введите строку: "))
		n=int(input("Введите число повторов: "))
		for i in range(0, n):
			result += str + '\n'
		return result

	def func46(self):
		m=int(input("Введите степень: "))
		return "%s в степени %s равно %s"%(self.x, m, self.x**m)

	def func79(self):
		result = ""
		x = self.x
		for i in range(0, 10):
			x+=1
			result+="%s \n" % x
		return result