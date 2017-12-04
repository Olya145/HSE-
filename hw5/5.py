with open("C:/Users/HP//Desktop/многобукв.txt", "w") as f:
    integ = list(input("Введите 7 чисел: "))
    for i in integ:
        for s in range(int(i)):
            f.write("X")
        f.write("\n")
