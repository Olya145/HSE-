print("Bведите слово: ")
word = input()
cypher = ""
c = "бвгджзйклмнпрстфхцчшщъь"
v = "аеёиоуыэюя"
for i in word:
    for x in c:
        if x == i:
            cypher += x
    for y in v:
        if y == i:
            cypher += i + "с" + i
print(cypher)
