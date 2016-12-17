x=int(input("Введите число от 1 до 9:"))
if 1<=x<=3:
    s=str(input("Введите строку:"))
    n=int(input("Введите кол-во повторов строки:"))
    i=0
    while i<n:
        print(s)
        i=i+1        
elif 4<=x<=6:
    m=int(input("Введите степень, в которую следует возвести число:"))
    print(x**m)

elif 7<=x<=9:
    i=0
    while i<10:
        x=x+1
        i=i+1
        print(x)
else:
    print("Ошибка ввода")
