word = input("Введите слово или фразу: ")
word = word.lower()
word = ''.join(e for e in word if e.isalnum())

if word == word[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром.")
