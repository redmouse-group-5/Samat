str=(input("Введите предложение:"))  
words={}
for w in str.split(" "):
    words[len(w)]=w

print(words.get(max(words)))