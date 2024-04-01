powergamer = input()
f = open("monster_game.csv", encoding="utf-8") #открытие файла
h = [i[:-1].split(",") for i in f.readlines()] #добавление строк файла в список из списков
del h[0] #удаление строки заголовка, здесь она нам не нужна
while powergamer != "хватит":
    count = 0 #счетчик монстров, которых может победить игрок
    for i in h:
        if int(powergamer) > int(i[3]) and i[3] != "0": #сравнение силы игрока и здоровья монстра
            count += 1
    if count > 0:
        print(f"Вы сможете победить: {count} монстров")
    else:
        print("Вы очень слабы. Сходите и наберитесь опыта!")
    powergamer = input()