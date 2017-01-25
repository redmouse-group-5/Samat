from Task_3 import task_1_2

print ("Вас приветствует программа Общество в начале XXI века")
a=int(input("Введите, пожалуйста, ваш возраст: "))
if 0<=a<=7:
    print (task_1_2.func17(a))
elif a<=18:
    print (task_1_2.func718(a))
elif a<=25:
    print (task_1_2.func1825(a))
elif a<=60:
    print (task_1_2.func2560(a))
elif a<=120:
    print (task_1_2.func60120(a))
else:
    print (task_1_2.error())