from abstr import Param

class task1_2(Param):
	param=0
	def __init__(self, age):
		print ("Вас приветствует программа Общество в начале XXI века")
		self.age = age
		if 0<=self.age<=7:
		    print (self.func17())
		elif self.age<=18:
		    print (self.func718())
		elif self.age<=25:
		    print (self.func1825())
		elif self.age<=60:
		    print (self.func2560())
		elif self.age<=120:
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