str=(input("Уважаемый пользователь, введите предложение. Вместо пробелов, пожалуйста, используйте символ ;"))  
words={}
for w in str.split(";"):
    words[len(w)]=w

print(words.get(max(words)))