#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов
from itertools import zip_longest
text1=str(open('file1.txt', 'r').read()).split('+') #получаем списки с разделением по членам
text2=str(open('file2.txt', 'r').read()).split('+')

text1.reverse()
text2.reverse()

for i,j in zip_longest(text1, text2, fillvalue=0):
    