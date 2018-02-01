print("Введите фразу или слово для перевода на Pig Latin: ")
line = input()
word = line.split(' ')
cypher = ""
c = "bcdfghjklmnpqrstvwxz"
v = "aeiouy"
for z in word:
        i = 0
        for x in c:
            if x == z[0] and x == z[1]:
                i += 2
            elif x == z[0]:
                i += 1
        for y in v:
            if y == z[0]:
               i += 3
        if i == 1:
            cypher += z[1::] + z[0] + "ay" + " "
        if i == 2:
            cypher += z[2::] + z[:2] + "ay" + " "
        if i == 3:
            cypher += z + "way" + " "
print(cypher)
