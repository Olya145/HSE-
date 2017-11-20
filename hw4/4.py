with open("C:/Users/HP/Desktop/text.txt") as f:
    text = f.read().split(' ')
    i = 0
    for s in text:
       if s.istitle():
            i = i + 1
    print("Процент слов, написанных с большой буквы: %.2f %%" %(i/len(text)*100))
