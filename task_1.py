from Task_3 import task_1

x=int(input("Введите, пожалуйста, число x: "))
if 0<=x<=3:	
	print (task_1.func13(x))
elif 4<=x<=6:
	print (task_1.func46(x))
elif 7<=x<=9:
	print (task_1.func79(x))
else:
    print ("Error")