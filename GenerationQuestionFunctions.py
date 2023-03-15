from random import randint, choice

#Генерация типа задачи
def generation_type(types):
    return choice(types)

#Генерация чисел для 1 типа
def generation_type_1(difficulty):
    return [randint(1, 100 ** difficulty), randint(2, 10), randint(2, 10)]

#Генерация чисел для 2 типа
def generation_type_2(difficulty):
    resoult = []
    minim = 1
    maxim = 100 ** difficulty
    for i in range(randint(2 ** (difficulty - 1), 2 ** difficulty)):
        resoult.append([randint(minim, maxim), randint(2, 10),
                        choice(['+', '-', '*', '/'])])
    return resoult


        
    
