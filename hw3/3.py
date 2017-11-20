word = list(input("Ввод слова: "))
print("".join(word))
for i, sym in enumerate(word):
    word = word[1:]
    word1="".join(word)
    print(word1)
