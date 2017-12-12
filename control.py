with open ("C:/Users/student/Desktop/Ozhegov.txt", encoding = "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        word = line.split("|")
        if len(word[0]) >= 20: 
                print(line)
        


    
    

    
