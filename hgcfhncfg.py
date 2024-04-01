f = open("monster_game.csv", encoding="utf-8")
h = [i[:-1].split(",") for i in f.readlines()]
d = []
maxregen = 0 #переменная для максимальной регенерации
maxpower = 0 #переменная для максимального доп.хода
maxattack = 0 #переменная для максимальной атаки
for i in h:
    if i[1] == "регенерация":
        regen = (int(i[6]) * (int(i[2]) / 100))
        if regen > maxregen:
             maxregen = regen #поиск максимальной регенерации
    elif i[1] == "дополнительный ход":
        power = (int(i[2]) + int(i[3]) + int(i[4]) + int(i[5]) + int(i[6])) * (int(i[2]) / 100)
        if power > maxpower:
            maxpower = power #поиск максимального дополнительного хода
    elif i[1] == "усиление атаки":
        attack = int(i[3]) * (int(i[2]) / 100)
        if attack > maxattack:
            maxattack = attack #поиск максимальной атаки

t = open("monster_opportunity.csv", mode="w", encoding="utf-8")
t.write(f"opportunity, power \n")
t.write(f"Регенерация, {maxregen} \n")
t.write(f"Дополнительный ход, {maxpower} \n")
t.write(f"Усиление атаки, {maxattack} \n") #создание и заполнение нового файла monster_opportunity

print(f"Регенерация: {maxregen}")