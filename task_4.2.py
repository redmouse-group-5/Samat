import random
answer= ["Да", "Безусловно да", "О да", "Вполне возможно", "Абсолютно", "Всегда", "Разумеется", "Конечно"]
while True:
	ask = (input("Задайте ваш вопрос: "))
	print ("%s - %s"%(ask, random.choice(answer)))
	exit = (input('Еще раз (Y/N)? '))
	if exit == 'N' or exit=='n':
		break
