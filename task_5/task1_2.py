class task1_2():
	
	def __init__(self, a):
		print ("Вас приветствует программа Общество в начале XXI века")
		self.a = a
		if 0<=self.a<=7:
		    print (self.func17())
		elif self.a<=18:
		    print (self.func718())
		elif self.a<=25:
		    print (self.func1825())
		elif self.a<=60:
		    print (self.func2560())
		elif self.a<=120:
		    print (self.func60120())
		else:
		    print (self.error())

	def func17(self):
	    return "Вам в детский сад"

	def func718(self):
	    return "Вам в школу"

	def func1825(self):
	    return "Вам в профессиональное учебное заведение"

	def func2560(self):
	    return "Вам на работу"
	
	def func60120(self):
	    return "Вам предоставляется выбор"

	def error(self):
	    error = "Error"
	    return error*3