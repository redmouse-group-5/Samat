str1=(input("Уважаемый пользователь, введите предложение:"))
str2=(input("Уважаемый пользователь, введите знак выделения короткого слова:"))
words={}
for w in str1.split(" "):
    words[len(w)]=w

print(str2+words.get(min(words)))