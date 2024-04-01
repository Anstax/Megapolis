f = open("monster_game.csv", encoding="utf-8") #открытие файла
h = [i[:-1].split(",") for i in f.readlines()] #добавление строк файла в список из списков
del h[0]
sl = {} #создание словаря для хранения ключей и значений
for i in h: #заполнение словаря
    name, clas = i[0].split(" ")
    if i[1] != "регенерация":
        opp1, opp2 = i[1].split(" ")
        key = name + clas + opp1 + opp2 + i[2]
    else:
        key = (name + clas + i[1] + i[2])
    if key not in sl:
        sl[key] = i[1]

for j in sl.keys(): #вывод значений в запрошенном виде
    print(f"{j} - {sl[j]}")