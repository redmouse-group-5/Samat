import os, time

def get_info(path):
	result = list()
	if os.path.exists(path):
		result.append("Размер %s"%os.path.getsize(path))
		result.append("Дата создания %s"%time.ctime(os.path.getmtime(path)))
		result.append("Путь %s"%os.path.abspath(path))
		if os.path.isdir(path):
			result.append("Тип: расположение")
		else:
			result.append("Тип: файл")
		
	else:
		result.append("Ничего не найдено %s"%path)
	return result

path = (input("Введите путь "))
fname = (input("Введите название файла/папки "))

full_name=os.path.join(path, fname)

print ("\n".join(get_info(full_name)))
