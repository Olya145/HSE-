import random
d = {}
with open("word.csv", encoding='utf-8') as f:
    for line in f:
        line = line.rstrip()
        if(line != "word,wordhelpone,wordhelptwo,wordhelpthree,wordhelpfour,wordhelpfive"):
            parserLine = line.split(',')
            d[parserLine[0]] = parserLine[1:6]

wordInt = random.randint(0,4)
word = list(d.keys())[wordInt]
helpWord = d[word][random.randint(0,4)]
print("Угадайте существиельное\n"+helpWord+" ...")
tryCounter = 3
checker = False
while (checker!=True):
    if(input() == word):
        checker = True
    else:
        if(tryCounter == 1):
            break;
        else:
            tryCounter-=1
            print("Вы ввели неправильное слово! У вас осталось ",tryCounter, " попытки!")
            
if(checker):
    print("Вы верно угадали слово!")
else:
    print("Вы исчерпали все попытки!")
