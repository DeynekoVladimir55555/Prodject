import sqlite3

con = sqlite3.connect("DataBase.db")

cur = con.cursor()
#Поиск по базе данных
def find(operand):
    return cur.execute(operand).fetchall()[0]
#Поиск статистики
def statistics():
    resoult_true = cur.execute('''SELECT id FROM QuestionAnswers WHERE
                            werdict="True"''').fetchall()
    resoult_false = cur.execute('''SELECT id FROM QuestionAnswers WHERE
                            werdict="False"''').fetchall()
    true = len(resoult_true)
    false = len(resoult_false)
    return [str(true), str(false)]
#Сохранение настроек при изменении
def update(difficulty, types):
    cur.execute('''UPDATE QuestionSettings
                    SET difficulty = ?,
                        type1 = ?,
                        type2 = ?''', (difficulty, str(types[0]), str(types[1])))
    con.commit()
#Внос новой статистики
def insert(werd):
    if werd == 'True':
        cur.execute('''INSERT INTO QuestionAnswers(werdict) VALUES('True')''')
    else:
        cur.execute('''INSERT INTO QuestionAnswers(werdict) VALUES('False')''')
    con.commit()
#Очистка статистики
def delete():
    cur.execute('''DELETE from QuestionAnswers''')
    con.commit()
