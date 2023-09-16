'''
С клавиатуры вводится строка. Напишите выражение для генерации
словаря, который содержит информацию о частоте употребления букв в заданной строке.
При анализе не учитывайте регистр, а ключами словаря сделайте использованные в строке
буквы в нижнем регистре.
'''

string = input()
d = {}
for i in set(string):
    d[i] = string.count(i)
if ' ' in d: del d[' ']
print(string, d, sep='\n')
