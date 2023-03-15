#Перевод из 10 системы счисления
def translate_from_ten(number, sistem):
    res = ''
    while number > 0:
        res += str(number % sistem)
        number //= sistem
    return res[::-1]

#Перевод в 10 систему счисления
def translate_to_ten(number, sistem):
    res = 0
    k = 0
    for elem in str(number)[::-1]:
        res += int(elem) * sistem ** k
        k += 1
    return res

