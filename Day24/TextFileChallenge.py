with open("D:/Python Practice/DAY1-Practice/Day24/Names.txt") as file:
    Names_list= [line.strip() for line in file]
    for name in Names_list:
        with open(f"D:/Python Practice/DAY1-Practice/Day24/Person_{name}.txt", mode="w") as file:
            file.write(name)
