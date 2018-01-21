import random

def pronoun():
    with open("text_1.txt", encoding="utf-8") as f:
         lines = f.readlines()
         for line in lines:
             pronouns = line.split(" ")
         return random.choice(pronouns)

def verb():
    with open("text_2.txt", encoding="utf-8") as f:
         lines = f.readlines()
         for line in lines:
             verbs = line.split(" ")
    return random.choice(verbs)

def noun():
    with open("text_3.txt", encoding="utf-8") as f:
         lines = f.readlines()
         for line in lines:
             nouns = line.split(",")
         return random.choice(nouns)        

def verb2():
    with open("text_4.txt", encoding="utf-8") as f:
         lines = f.readlines()
         for line in lines:
             verbs2 = line.split(" ")
         return random.choice(verbs2)

def random_sentence():
    sentence = [pronoun() + " " + verb() + " gern " + noun() + '.', pronoun() + " " + verb() + " night" + '.', verb2() + " " + pronoun() + " " + noun() + "?", verb2() + " bitte" + "!", "Wenn " + pronoun() + " " + verb() + " " + noun() + "!"] 
    return sentence

num_of_sents = random.randint(1, 4) 
for i in range(num_of_sents):  
    sentence = random_sentence()
    print(" ".join(sentence), end=' ') 
    
